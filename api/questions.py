from fastapi import APIRouter

router = APIRouter()

@router.post("/questions/generate", tags=["questions"])
def generate_prompt_question():
    from libs.ai_model import generate_prompt_question

    question = generate_prompt_question()

    return {
        "message": "Prompt question generated successfully",
        "data": {
            "question": question
        }
    }