from flask import Flask, jsonify, request, abort
from llama_cpp import Llama
import os

app = Flask(__name__)

"""
Documentation: https://llama-cpp-python.readthedocs.io/en/latest/api-reference/#llama_cpp.Llama.create_chat_completion
Payload:
{
    max_tokens: 32, # Generate up to 32 tokens, set to None to generate up to the end of the context window
    messages: [
          {"role": "system", "content": prompt_content},
          {
              "role": "user",
              "content": task_content
          }
      ]
}
"""

llm = Llama(
    model_path=os.path.join(os.path.dirname(__file__), "models", "llama-2-7b-chat.Q4_K_M.gguf"),
    n_gpu_layers=-1, # Uncomment to use GPU acceleration
    seed=1338, # Uncomment to set a specific seed
    n_ctx=2048, # Uncomment to increase the context window
    chat_format="llama-2"
)


@app.route('/chat', methods=['POST'])
def chat():
    if not request.json:
        abort(400)

    output = llm.create_chat_completion(
        max_tokens = request.json["max_tokens"],
        messages = request.json["messages"]
    )

    return jsonify(output), 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
