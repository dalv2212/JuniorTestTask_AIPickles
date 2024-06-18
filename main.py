from fastapi import FastAPI, HTTPException
import uvicorn

from schemas import SummarizeRequest, SummarizeOutput
from service import Summarize

tags_metadata = [
    {
        "name": "summarize",
        "description": "Send a POST request with a JSON body containing the text to be summarized.",
    },
]

app = FastAPI(
    openapi_tags=tags_metadata,
    title="JuniorTestTask AI Pickles",

)


# Summarization route
@app.post("/summarize", tags=["summarize"])
async def summarize(request: SummarizeRequest) -> SummarizeOutput:
    summarizer = Summarize()
    try:
        # Getting text from a query
        text = request.text

        # Performing summation
        summary = summarizer.summarize(text)

        # Пreturning the result in JSON format
        return SummarizeOutput(summary=summary)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
