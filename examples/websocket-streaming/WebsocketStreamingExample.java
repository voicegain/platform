/**
MIT License

Copyright (c) 2020 Voicegain (Resolvity, Inc.)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

 */

package ai.voicegain.zendesk;

import java.io.IOException;

import java.nio.ByteBuffer;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.concurrent.TimeUnit;

import okhttp3.HttpUrl;
import okhttp3.MediaType;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;
import okhttp3.WebSocket;
import okhttp3.WebSocketListener;
import okio.ByteString;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.JsonMappingException;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;

public class WebsocketStreamingExample  {
	
	private static final String urlString = "https://api.voicegain.ai/v1/asr/transcribe/async"; // url to transcribe API
	private static final String JWT = "<<your JWT here>>";
	private static final String PATH_BASE = "./src/test/resources/";  // where the audio files are located

	private static final int NORMAL_CLOSURE_STATUS = 1000;
	
	/*
	 * The Websocket listener
	 */
	static private class MyListener extends WebSocketListener {
		
		private final String name;
		
		public MyListener(String name) {
			this.name = name;
		}
		
		private long startTs = System.currentTimeMillis();
		
		public long setStartTs() {
			startTs = System.currentTimeMillis();
			return startTs;
		}
		
		@Override
		public void onOpen(WebSocket  session, Response response) {
			System.out.println(name+"\topened session: " + session);
		}
		
		@Override
	    public void onMessage( WebSocket webSocket, ByteString bytes) {
			System.out.println("\r\n"+name+"\treceived ("+(System.currentTimeMillis()-startTs)+"): "+bytes.toString());
		}
		
		@Override
		public void onMessage(WebSocket webSocket, String text) {
			System.out.println("\r\n"+name+"\treceived ("+(System.currentTimeMillis()-startTs)+"): "+text);
		}

		@Override
		public void onClosed(WebSocket webSocket, int code, String reason) {
			System.out.println(name+"\tclosed: "+webSocket+" "+code+" "+reason);
		}

		@Override
		public void onClosing(WebSocket webSocket, int code, String reason) {
			webSocket.close(NORMAL_CLOSURE_STATUS, null);
			System.out.println(name+"\tclosing: "+webSocket+" "+code+" "+reason);
		}

		@Override
		public void onFailure(WebSocket webSocket, Throwable t, Response response) {
			System.out.println(name+"\tfailure: "+webSocket+" "+t);
		}		
	}
	
	/**
	 * payload of the request to Voicegain
	 */
	private static String json1 = "{\r\n" + 
			"  \"sessions\": [{\r\n" + 
			"     \"asyncMode\": \"REAL-TIME\",\r\n" + 
			"     \"websocket\": { \"useSTOMP\" : false, \"adHoc\":true, \"minimumDelay\":0 },\r\n" + 
			"     \"content\": {\"incremental\":[\"words\"]}\r\n" +
			"  }],\r\n" + 
			"  \"audio\": {\r\n" + 
			"    \"source\": { \"stream\": { \"protocol\": \"WEBSOCKET\" } },\r\n" + 
			"    \"format\": \"__FORMAT__\",\r\n" + 
			"    \"rate\": __RATE__,\r\n" + 
			"    \"channel\": \"mono\",\r\n" + 
			"    \"capture\" : false\r\n" + 
			"  },\r\n" + 
			"  \"settings\": {\r\n" + 
			"    \"asr\": {\r\n" + 
			"      \"noInputTimeout\": 5000,\r\n" + 
			"      \"completeTimeout\": 1000\r\n" + 
			"    }\r\n" + 
			"  }\r\n" + 
			"}";


	/**
	 * helper method for sending binary audio over websocket	
	 * @param ws
	 * @param array
	 * @param offset
	 * @param length
	 * @return
	 * @throws Exception
	 */
	static public boolean send(WebSocket ws, byte[] array, int offset, int length) throws Exception {
		System.out.print('.');
		ByteBuffer bb = ByteBuffer.wrap(array,offset,length);
		try {
			ws.send(ByteString.of(bb));
			return true;
		} catch (IllegalStateException e) {
			System.out.println("Assuming the other side closed the Websocket");
			return false;
		}
	}
	
	/**
	 * MAIN
	 * @param args
	 * @throws Exception
	 */
	public static void main(String[] args) throws Exception {
		System.out.println("START");
		
        // test file is available here: 
        // https://s3.us-east-2.amazonaws.com/files.public.voicegain.ai/4_8_1_6_9.wav
		runTest("4_8_1_6_9.wav", "L16", 8000, 2, 44);
		// add additional tests here
		
		System.out.println("THE END");
	}


	/**
	 * 
	 * @param fname
	 * @param format
	 * @param rate
	 * @param bytesPerSample
	 * @param wavHeaderLen length of the audio header - the header should not be streamed, only the audio bytes
	 * @throws IOException
	 * @throws JsonProcessingException
	 * @throws JsonMappingException
	 * @throws Exception
	 * @throws InterruptedException
	 */
	private static void runTest(String fname, String format, int rate, int bytesPerSample, int wavHeaderLen)
			throws IOException, JsonProcessingException, JsonMappingException, Exception, InterruptedException {
		
		System.out.println("");
		System.out.println("BEGIN runTest("+fname+", "+format+", "+rate+", "+bytesPerSample+")");
		
		String payload = json1.replace("__FORMAT__", format).replace("__RATE__", ""+rate).replace("__GRAMMAR_NAME__", fname.replace('.', '-'));
		System.out.println("Making request to: "+urlString+" with payload:");
		System.out.println(payload);

		HttpUrl.Builder urlBuilder = HttpUrl.parse(urlString).newBuilder();
		okhttp3.Request request = new Request.Builder()
	             .header("authorization", "Bearer " + JWT)
	             .header("content-encoding", "UTF-8")
	             .header("accept", "application/json")
	             .post(okhttp3.RequestBody.create(payload, MediaType.parse("application/json")))
                .url(urlBuilder.build())
                .build();
		
		OkHttpClient httpClient =  new OkHttpClient();
		long beforeHttpRequest = System.currentTimeMillis();
		okhttp3.Response httpResponse = httpClient.newCall(request).execute();
		long afterHttpRequest = System.currentTimeMillis();
		long timeForHttpRequest = afterHttpRequest - beforeHttpRequest;
		
		String	response = httpResponse.body().string();

		System.out.println("took "+timeForHttpRequest+" msec to obtain response: "+response);
		
		ObjectMapper mapper = new ObjectMapper();
		
		JsonNode root = mapper.readTree(response);
		
		JsonNode audio = root.get("audio");
		
		JsonNode stream = audio.get("stream");
		
		String wssUrlStr = stream.get("websocketUrl").asText();
		
		System.out.println("websocket url: "+wssUrlStr);
		
		String outputUrl = "";  
		JsonNode sessions = root.get("sessions");
		for (int index=0; index < sessions.size(); index++) {
			JsonNode session = sessions.get(index);
			JsonNode websocket = session.get("websocket");
			if (websocket != null) {
				JsonNode url = websocket.get("url");
				if (url != null) {
					outputUrl = url.asText();
					System.out.println("result output url: " + outputUrl);
					break;
				}
			}
		}
		
		final Path audioFile = Paths.get(PATH_BASE + fname);
		System.out.println("reading from: "+audioFile);
		byte [] audioData=Files.readAllBytes(audioFile);
		
		System.out.println("read "+audioData.length+" bytes");
		
		// open audio streaming websocket
		OkHttpClient audioClient = new OkHttpClient.Builder()
                .readTimeout(0, TimeUnit.MILLISECONDS)
                .build();

        Request audioRequest = new Request.Builder()
                .url(wssUrlStr)
                .build();

        // open websocket for receiving recognition results
        WebsocketStreamingExample.MyListener audioListener = new WebsocketStreamingExample.MyListener("audio");
        WebSocket audioWebSocket = audioClient.newWebSocket(audioRequest, audioListener);

		OkHttpClient resultsClient = new OkHttpClient.Builder()
                .readTimeout(0, TimeUnit.MILLISECONDS)
                .build();

        Request resultsRequest = new Request.Builder()
                .url(outputUrl)
                .build();

        WebsocketStreamingExample.MyListener resultsListener = new WebsocketStreamingExample.MyListener("result");
        WebSocket resultsWebSocket = resultsClient.newWebSocket(resultsRequest, resultsListener);		

		// skip over audio header
		System.out.println(""+(char)audioData[0]);
		System.out.println(""+(char)audioData[1]);
		System.out.println(""+(char)audioData[2]);
		System.out.println(""+(char)audioData[3]);
		int i=wavHeaderLen;
		//System.out.println(""+(char)audioData[i-6]);
		//System.out.println(""+(char)audioData[i-5]);
		System.out.println(""+(char)audioData[i-4]);
		System.out.println(""+(char)audioData[i-3]);
		System.out.println(""+(char)audioData[i-2]);
		System.out.println(""+(char)audioData[i-1]);
		
		final int bytesPerMsec = (bytesPerSample*rate) / 1000;
		long count = 0;
		boolean otherSideClosed = false;
		long start = resultsListener.setStartTs();
		// send audio over websocket at approximately real-time rate
		for(; i<audioData.length-1000; i+=1000) {
			if(!send(audioWebSocket, audioData, i, 1000)) {
				otherSideClosed = true;
				System.out.println("other side closed - Stopping sending at count="+count+" elapsed="+(System.currentTimeMillis() - start)+" msec");
				break;
			}
			count += 1000;
			long expectedElapsed = count / bytesPerMsec;
			long elapsed = System.currentTimeMillis() - start;
			long diff = expectedElapsed - elapsed;
			if(diff > 0) {
				Thread.sleep(diff);
			}
			
		}
		if(!otherSideClosed) {
			int remain = audioData.length-i;
			if(remain>0) {
				System.out.println("sending remaining: "+remain);
				if(!send(audioWebSocket, audioData, i, remain)) {
					otherSideClosed = true;
					System.out.println("other side closed");

				}
			}
		}
		System.out.println("finished streaming after "+(System.currentTimeMillis()-start)+"ms");
		//wait a little for streaming and processing to complete
		Thread.sleep(6000);
		audioWebSocket.close(NORMAL_CLOSURE_STATUS+1, "audio-end");
		
		Thread.sleep(100);
		resultsWebSocket.close(NORMAL_CLOSURE_STATUS+2, "results-end");

		System.out.println("END runTest("+fname+", "+format+", "+rate+", "+bytesPerSample+")");
	}

}
