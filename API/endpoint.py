from fastapi  import FastAPI,Response
from . import schema
from . import endpoint
from Combined_script.combined_script import initialize_model_embedding_vector_ragchain,question_answer,chat_history

app =FastAPI()


llm_model,coversational_chain_history = initialize_model_embedding_vector_ragchain()

@app.post("/chat",response_model=schema.answer)
async  def question_answering(question : schema.question):
    answer = question_answer(llm_model,question.question)
    return {'answer': answer}


@app.get("/chat_history")
async  def llm_chat_history():
    history = chat_history(llm_model)
    # return history
    return {'history': history}


