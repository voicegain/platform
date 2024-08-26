from fastapi import FastAPI, HTTPException
from model import *
from fast_food_bot import CHAIN, MEMORY_HISTORY_STORE

app = FastAPI()


@app.post("/bot")
async def create_session(request: TelephonyBotPostReq):
    sid = request.sid
    csid = f"bot-{sid}"
    return TelephonyBotPostPutResp(
        csid=csid,
        sid=sid,
        question=Question(
            text="Thank you for calling Big Burger. What can I do for you today?"
        )
    )


@app.put("/bot")
async def update_session(request: TelephonyBotPutReq):
    csid = request.csid
    sid = request.sid
    bot_answer = None
    user_input = None

    if request.events:
        for event in request.events:
            if isinstance(event, InputEvent):
                if event.vuiResult == "MATCH":
                    if event.vuiAlternatives:
                        user_input = event.vuiAlternatives[0].utterance
                else:
                    print(f"Get vuiResult {event.vuiResult}")
                break

    if user_input:
        bot_answer = CHAIN.invoke(
            {"input": user_input},
            config={'configurable': {'session_id': csid}}
        )["output"]

    if bot_answer is None:
        return TelephonyBotPostPutResp(
            csid=csid,
            sid=sid,
            question=Question(
                text="Sorry, I didn't get that. Can you say it again?"
            )
        )
    else:
        return TelephonyBotPostPutResp(
            csid=csid,
            sid=sid,
            question=Question(
                text=bot_answer
            )
        )


@app.delete("/bot")
async def delete_session(request: TelephonyBotDeleteReq):
    csid = request.csid
    result = MEMORY_HISTORY_STORE.pop(csid, None)
    if result:
        return TelephonyBotDeleteResp(
            csid=csid,
            termination="Success"
        )
    else:
        return TelephonyBotDeleteResp(
            csid=csid,
            termination="Session not found"
        )


@app.get("/bot")
async def root():
    return {"message": "Welcome to the Fast Food Ordering Service"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
