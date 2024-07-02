import requests, time, os, json, re
import configparser

## Note: rate-limit (429 code) handling is only partially implemented in this script

cfg = configparser.ConfigParser()
cfg.read("config.ini")
configSection = cfg.get("DEFAULT", "CONFIG")
protocol = cfg.get(configSection, "PROTOCOL")
hostPort = cfg.get(configSection, "HOSTPORT")
JWT = cfg.get(configSection, "JWT")
urlPrefix = cfg.get(configSection, "URLPREFIX")
inputFolder = cfg.get("DEFAULT", "INPUTFOLDER")
inputFname = cfg.get("DEFAULT", "INPUTFILE")
outputFolder = cfg.get("DEFAULT", "OUTPUTFOLDER")

#model = "VoiceGain-omega"
model = "VoiceGain-omega-x"

print("model: {}".format(model))

if not os.path.exists(outputFolder):
    os.makedirs(outputFolder)

host = f"{protocol}://{hostPort}/{urlPrefix}"

print("host: {}".format(host))  

asr_body = {
    "sessions": [
        {
            "asyncMode": "OFF-LINE",
            #"initialPrompt": "I am talking to a customer support agent.",
            #"audioChannelSelector" : "left",
            #"initialPrompt": "I am a support Agent talking to a customer.",
            "audioChannelSelector" : "mix",
            "poll": {
                # will delete the session after 1 minute
                #"afterlife": 60000
                "persist" : 600000
            },
            "content": {
                #"incremental": ["progress"],
                "full" : ["words", "transcript"]
            }
        }
    ],
    "audio":{
        "source": {
            "dataStore": {
                "uuid": "to be filled later"
            }
        }
    },
    "settings": {
        "asr": {
            #"languages" : ["es", "en"],
            "languages" : ["en"],
            "acousticModelNonRealTime" : model,
            "confidenceThreshold" : 0.01,
            "noInputTimeout": -1,
            "completeTimeout": -1,
            "sensitivity" : 0.5,
            "hints" : [
        "1025SEP[1025_SCP|1025_S_EP|1025_SE_P|1025_S_E_P|10_25_SEP|10_25_S_EP|10_25_SE_P|10_25_S_E_P]:10",
        "1050HC[10_50_HC|1050_HC|1050_H_C|10_50_H_C]:10",
        "1055CW[10_55_CW|1055_CW|1055_C_W|10_55_C_W]:10",
        "1060NHHI[1060_NHHI|1060_N_HHI|1060_NH_HI|1060_NHH_I|1060_NH_HI|1060_NHH_I|1060_N_H_H_I|10_60_NHHI|10_60_N_HHI|10_60_NH_HI|10_60_NHH_I|10_60_NH_HI|10_60_NHH_I|10_60_N_H_H_I]:10",
        "1070NP[1070_NP|1070_N_P|10_70_NP|10_70_N_P]:10",
        "ACH[A_CH|A_CH|A_C_H]:10",
        "ADPT[A_DPT|AD_PT|ADP_T|A_D_P_T|AD_PT|AD_P_T|ADP_T]:10",
        "AGI[A_GI|AG_I|A_G_I]:10",
        "AHT[A_HT|AH_T|A_H_T]:10",
        "AIP[A_IP|AI_P|A_I_P]:10",
        "AL[A_L]:10",
        "APC[AP_C|A_PC|A_P_C]:10",
        "APCR[A_PCR|AP_CR|APC_R|A_P_CR|A_P_C_R|AP_C_R|APC_R]:10",
        "APP[AP_P|A_PP|A_P_P]:10",
        "APPID[A_P_P_I_D|AP_P_I_D|APP_I_D|APPI_D|AP_PID|APP_ID|A_P_P_ID]:10",
        "AR[A_R]:10",
        "ARD[A_RD|AR_D|A_R_D]:10",
        "BC[B_C]:10",
        "BI[B_I]:10",
        "CB[C_B]:10",
        "CC[C_C]:10",
        "CCR[C_CR|CC_R|C_C_R]:10",
        "COC[C_OC|CO_C|C_O_C]:10",
        "COI[C_OI|CO_I|C_O_I]:10",
        "CRM[C_RM|CR_M|C_R_M]:10",
        "CSSI[CS_SI|C_SSI|C_S_SI|C_S_S_I|CS_S_I|CSS_I]:10",
        "CW[C_W]:10",
        "DA[D_A]:10",
        "DC[D_C]:10",
        "DCF[D_CF|DC_F|D_C_F]:10",
        "DD[D_D]:10",
        "DOB[D_OB|DO_B|D_O_B]:10",
        "FLDOE[FL_DOE|F_L_D_O_E|FLD_OE]:10",
        "WVDOE[WV_DOE|W_V_D_O_E|WVD_OE]:10",
        "DOR[D_OR|DO_R|D_O_R]:10",
        "DOS[D_OS|DO_S|D_O_S]:10",
        "DPC[D_PC|DP_C|D_P_C]:10",
        "DPCR[DPCR|D_PCR|DP_CR|DPC_R|DP_C_R|D_P_C_R]:10",
        "DX[D_X]:10",
        "ECF[E_CF|EC_F|E_C_F]:10",
        "EE[E_E]:10",
        "EFT[E_FT|EF_T|E_F_T]:10",
        "ELA[E_LA|EL_A|E_L_A]:10",
        "EMA[E_MA|EM_A|E_M_A]:10",
        "ER[E_R]:10",
        "ESA[E_SA|ES_A|E_S_A]:10",
        "FDPIR[FD_PIR|FDP_IR|F_D_P_I_R]:10",
        "FDS[F_DS|FD_S|F_D_S]:10",
        "FEFP[F_EFP|FE_FP|FEF_P|FE_F_P|FEF_P|F_E_F_P]:10",
        "FES[F_ES|FE_S|F_E_S]:10",
        "FES-EO[FESEO|FES_EO|F_E_S_E_O]:10",
        "FES-UA[FESUA|FES_UA|F_E_S_U_A]:10",
        "FLEID[FLE_ID|F_L_E_I_D]:10",
        "FS[F_S]:10",
        "FSA[F_SA|FS_A|F_S_A]:10",
        "FTC[F_TC|FT_C|F_T_C]:10",
        "GED[G_ED|GE_D|G_E_D]:10",
        "HA[H_A]:10",
        "HSH[H_SH|HS_H|H_S_H]:10",
        "HUD[H_UD|HU_D|H_U_D]:10",
        "IC[I_C]:10",
        "IEP[I_EP|IE_P|I_E_P]:10",
        "INS[I_NS|IN_S|I_N_S]:10",
        "IRA[I_RA|IR_A|I_R_A]:10",
        "IRS[I_RS|IR_S|I_R_S]:10",
        "JAX[J_AX|JA_X|J_A_X]:10",
        "KG[K_G]:10",
        "LES[L_ES|LE_S|L_E_S]:10",
        "MEP[M_EP|ME_P|M_E_P]:10",
        "MSID[M_SID|M_S_ID|M_S_I_D|MS_ID|MS_I_D|M_S_I_D]:10",
        "MSS[M_SS|MS_S|M_S_S]:10",
        "NRI[N_RI|NR_I|N_R_I]:10",
        "NW[N_W]:10",
        "OA[O_A]:10",
        "OFA[O_FA|OF_A|O_F_A]:10",
        "OH[O_H]:10",
        "OHR[O_HR|OH_R|O_H_R]:10",
        "OHRUR[OHR_UR|OHRU_R|O_H_R_U_R]:10",
        "OLA[O_LA|OL_A|O_L_A]:10",
        "PC[P_C]:10",
        "POA[P_OA|PO_A|P_O_A]:10",
        "POR[P_OR|PO_R|P_O_R]:10",
        "PP[P_P]:10",
        "PRE-K[PREK|PRE_K|P_R_E_K]:10",
        "PS[P_S]:10",
        "QTR[Q_TR|QT_R|Q_T_R]:10",
        "RC[R_C]:10",
        "S8[S_8]:10",
        "SAS[S_AS|SA_S|S_A_S]:10",
        "SC[S_C]:10",
        "SCF[S_CF|SC_F|S_C_F]:10",
        "SY[S_Y]:10",
        "SFO[S_FO|SF_O|S_F_O]:10",
        "SME[S_ME|SM_E|S_M_E]:10",
        "SNAP[S_NAP|S_N_AP|S_N_A_P|SN_AP|SN_A_P|SNA_P]:10",
        "SP[S_P]:10",
        "SSA[S_SA|SS_A|S_S_A]:10",
        "SSI[S_SI|SS_I|S_S_I]:10",
        "SSN[S_SN|SS_N|S_S_NI]:10",
        "SUFS[S_UFS|S_U_FS|S_U_F_S|SU_FS|SU_F_S|SUF_S]:10",
        "SUP[S_UP|SU_P|S_U_P]:10"
            ]
            #, "diarization" : {
            #  "minSpeakers" : 2,
            #  "maxSpeakers" : 2
            #}
        }
        ,"formatters" : [
        {
            "type": "digits"
        }
        # ,{
        #     "type": "basic",
        #     "parameters": {"enabled": "true"}
        # },
        # , {
        #     "type": "enhanced",
        #     "parameters": {
        #         "CC": True,
        #         "SSN": True,
        #         "URL": True,
        #         "PHONE": True,
        #         "EMAIL": True
        #     }
        # }
        # , {
        #     "type": "profanity",
        #     "parameters": {"mask": "partial"}
        # }
        ,{
            "type": "spelling",
            "parameters": {"lang": "en-US"}
        }
        # ,{
        #     "type": "redact",
        #     "parameters": {
        #         "CC": "[CC]",
        #         "ZIP": "[ZIP]",
        #         "PERSON": "[PERSON]",
        #         "EMAIL" : "[EMAIL]",
        #         "PHONE" : "[PHONE]",
        #         "SSN" : "[SSN]",
        #         "DMY" : "[DMY]"
        #     }
        # }
        # ,{
        #     "type": "regex",
        #     "parameters": {
        #         "pattern": r"\b(January|February|March|April|May|June|July|August|September|October|November|December)\s+([1-9]|0[1-9]|[12][0-9]|3[01]),\s+\d{4}\b",
        #         "mask": "[DATE3]",
        #         "options": "IA"
        #     }
        # }  
        # ,{
        #     "type": "regex",
        #     "parameters": {
        #         "pattern": r"\b(January|February|March|April|May|June|July|August|September|October|November|December)\s+([1-9]|0[1-9]|[12][0-9]|3[01])(st|nd|rd|th),\s+\d{4}\b",
        #         "mask": "[DATE2]",
        #         "options": "IA"
        #     }
        # }  
        # ,{
        #     "type": "regex",
        #     "parameters": {
        #         "pattern": r"\b([1-9]|0[1-9]|[12][0-9]|3[01])(st|nd|rd|th)\s+of\s+(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{4}\b",
        #         "mask": "[DATE1]",
        #         "options": "IA"
        #     }
        # }            
        # ,{
        #     "type": "regex",
        #     "parameters": {
        #         "pattern": r"\b(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{2}\b",
        #         "mask": "[EXPD3]",
        #         "options": "IA"
        #     }
        # }            
        # ,{
        #     "type": "regex",
        #     "parameters": {
        #         "pattern": r"\b(January|February|March|April|May|June|July|August|September|October|November|December)(\s+of)?\s+\d{4}\b",
        #         "mask": "[EXPD2]",
        #         "options": "IA"
        #     }
        # }            
        # ,{
        #     "type": "regex",
        #     "parameters": {
        #         "pattern": r"\b(0[1-9]|1[0-2])\s([0-9]{2})\b",
        #         "mask": "[EXPD1]",
        #         "options": "IA"
        #     }
        # }            
        # ,{
        #     "type": "regex",
        #     "parameters": {
        #         "pattern": r"\b(0?[1-9]|1[0-2])\s(0?[1-9]|[12][0-9]|3[01])\s(19|20)\d{2}\b",
        #         "mask": "[DATE4]",
        #         "options": "IA"
        #     }
        # }  
        # ,{
        #     "type": "regex",
        #     "parameters": {
        #         "pattern": r"\b3[47][0-9]{13}\b",
        #         "mask": "[AMEX]",
        #         "options": "IA"
        #     }
        # }   
        # ,{
        #     "type": "regex",
        #     "parameters": {
        #         "pattern": r"\b(5[1-5][0-9]{14}|2[2-7][0-9]{14})\b",
        #         "mask": "[MC16]",
        #         "options": "IA"
        #     }
        # }   
        # ,{
        #     "type": "regex",
        #     "parameters": {
        #         "pattern": r"\b4\d{15}\b",
        #         "mask": "[VISA16]",
        #         "options": "IA"
        #     }
        # }   
        # ,{
        #     "type": "regex",
        #     "parameters": {
        #         "pattern": r"\b\d{4}\b",
        #         "mask": "[CVV4]",
        #         "options": "IA"
        #     }
        # }   
        # ,{
        #     "type": "regex",
        #     "parameters": {
        #         "pattern": r"\b\d{3}\b",
        #         "mask": "[CVV3]",
        #         "options": "IA"
        #     }
        # }   
        ]
    }
}

#### all settings above this line ####

audio_type = "audio/wav"

output_path = "{}/{}".format(outputFolder, time.strftime("%Y-%m-%d_%H-%M-%S"))
if not os.path.exists(output_path):
    os.makedirs(output_path)

data_url = "{}/data/file".format(host)

headers = {"Authorization":JWT}

def process_one_file(audio_fname):
    ## steps:
    ## 1. upload audio
    ## 2. start offline transcription session
    ## 3. keep polling untill we are done
    ## 4. retrieve transcript

    path, fname = os.path.split(audio_fname)

    print("Processing {}/{}".format(path,fname), flush=True)

    data_body = {
        "name" : re.sub("[^A-Za-z0-9]+", "-", fname),
        "description" : audio_fname,
        "contentType" : audio_type,
        "tags" : ["test"]
    }

    multipart_form_data = {
        'file': (audio_fname, open(audio_fname, 'rb'), audio_type),
        'objectdata': (None, json.dumps(data_body), "application/json")
    }
    print("uploading audio data {} ...".format(audio_fname), flush=True)
    
    data_response = None
    data_response_raw = None
    try:
        data_response_raw = requests.post(data_url, files=multipart_form_data, headers=headers)
        code = data_response_raw.status_code
        print("   response code: {}".format(code))

        if(code != 200 and code != 429):
            print("unexpected response code")
            print(data_response_raw.text)
            exit()

        resp_headers = data_response_raw.headers
        print("response headers: {}".format(resp_headers))

        ## note: ideally we should add rate-limit response handling also in the asr request
        if(code == 429):
            retry_after = resp_headers.get("Retry-After")
            if(retry_after is None):
                print("rate limit exceeded but response missing Retry-After")
                exit()
            return int(retry_after)

        data_response = data_response_raw.json()
    except Exception as e:
        print(str(data_response_raw))
        exit() 

    print("data response: {}".format(data_response), flush=True)

    if data_response.get("status") is not None and data_response.get("status") == "BAD_REQUEST":
        print("error uploading file {}".format(audio_fname), flush=True)
        exit()

    object_id = data_response["objectId"]
    print("objectId: {}".format(object_id), flush=True)

    ## test the rate limit
    # for i in range(10):
    #     get_response_raw = requests.get("{}/data/{}".format(host, object_id), headers=headers)
    #     get_response = get_response_raw.json()

    #     print("CHECK get response: {}".format(get_response), flush=True)

    #     code = get_response_raw.status_code

    #     if(code != 200 and code != 429):
    #         print("CHECK unexpected response code")
    #         exit()

    #     resp_headers = get_response_raw.headers
    #     print("CHECK response headers: {}".format(resp_headers))

    

    ## set the audio id in the asr request
    if not os.path.exists(output_path):
        os.mkdir(output_path)

    asr_body["audio"]["source"]["dataStore"]["uuid"] = object_id

    printTranscribeQueueStatus()

    print("making asr request ...", flush=True)
    asr_response_raw = requests.post("{}/asr/transcribe/async".format(host), json=asr_body, headers=headers)
    start_time = time.time()
    if(asr_response_raw.status_code != 200):
        print("unexpected response code {} for asr request".format(asr_response_raw.status_code), flush=True)
        print(asr_response_raw.text , flush=True)
        exit()

    asr_response = asr_response_raw.json()
    session_id = asr_response["sessions"][0]["sessionId"]
    polling_url = asr_response["sessions"][0]["poll"]["url"]

#    print("sessionId: {}".format(session_id)) #, flush=True)
#    print(" poll.url: {}".format(polling_url)) #, flush=True)

    # printTranscribeQueueStatus()

    index = 0
    ## poll untill we have final result
    while True:
        if(index == 0):
            #first
            print("no wait for first poll request")
        elif(index<5):
            time.sleep(0.3)
        else:
            time.sleep(4.9)

        elapsed_time = time.time() - start_time
        print("Time taken just before poll request:", elapsed_time, "seconds")
        poll_response_raw = requests.get(polling_url+"?full=false", headers=headers)
        elapsed_time = time.time() - start_time
        print("Time taken just after poll request:", elapsed_time, "seconds")

        code = poll_response_raw.status_code
        print("   response code: {}".format(code))

        if(code != 200 and code != 429):
            print("unexpected response code")
            exit()

        if(code == 429):
            retry_after = resp_headers.get("Retry-After")
            if(retry_after is None):
                print("rate limit exceeded but response missing Retry-After")
                exit()
            time.sleep(retry_after)
            continue

        poll_response = poll_response_raw.json()
        phase = poll_response["progress"]["phase"]
        is_final = poll_response["result"]["final"]
        print("Phase: {} Final: {}".format(phase, is_final), flush=True)

        # # write poll_response to JSON
        if(False):
            poll_response_path = os.path.join(output_path, "{}-{}-{}.json".format("audio_fname", session_id, index))
            with open(poll_response_path, 'w') as outfile:
                json.dump(poll_response, outfile)
            print("Phase: {} Final: {} -> Save result to {}".format(phase, is_final, poll_response_path), flush=True)

        index += 1
        if is_final:
            break

    # write full response
    if(True):
        poll_response_raw = requests.get(polling_url+"?full=true", headers=headers)
        print(poll_response_raw.headers['Content-Type'])
        poll_response = poll_response_raw.json()
        # write poll_response to JSON
        phase = poll_response["progress"]["phase"]
        print("Phase: {} Final: {}".format(phase, is_final), flush=True)
        poll_response_path = os.path.join(output_path, "{}--{}.json".format(session_id, index))
        with open(poll_response_path, 'w',  encoding='utf-8') as outfile:
            json.dump(poll_response, outfile, ensure_ascii=False)
        print("Save final result to {}".format(poll_response_path), flush=True)

    #get result as text file

    txt_url = "{}/asr/transcribe/{}/transcript?format=text".format(host, session_id)
    print("Retrieving transcript using url: {}".format(txt_url), flush=True)
    txt_response = requests.get(txt_url, headers=headers)
    txt_response.encoding = txt_response.apparent_encoding ## << needed to get the encoding correct
    transcript_text_path = os.path.join(output_path, "{}.txt".format(fname))
    with open(transcript_text_path, 'w',  encoding='utf-8') as file_object:
        file_object.write(txt_response.text)
    print("Save final transcript text to {}".format(transcript_text_path))
    print("", flush=True)

    printTranscribeQueueStatus()

    return -1

def printTranscribeQueueStatus():
    print("making asr queue request ...", flush=True)
    asr_response_raw = requests.get("{}/asr/transcribe/status/queue".format(host), headers=headers)
    if(asr_response_raw.status_code != 200):
        print("unexpected response code {} for asr request".format(asr_response_raw.status_code), flush=True)
    else:
        asr_response = asr_response_raw.json()
        pretty_asr_response = json.dumps(asr_response, indent=4)  # Pretty-printing here
        print("asr queue status:\n{}".format(pretty_asr_response), flush=True)

## MAIN ##

print("START", flush=True)

name = os.path.join(inputFolder, inputFname)
print("name: {}".format(name), flush=True)

retry_after = process_one_file(name)
while(retry_after >=0 ):
    print("rate-limit hit - need to wait {} seconds".format(retry_after), flush=True)
    time.sleep(retry_after)
    print("will retry now", flush=True)
    retry_after = process_one_file(name)


print("THE END", flush=True)