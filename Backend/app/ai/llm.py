import ollama


class LLM:

    MODEL = "llama3.2"  # pyright: ignore[reportUnannotatedClassAttribute]

    @staticmethod
    def generate(prompt: str) -> str:

        response = ollama.chat(  # pyright: ignore[reportUnknownMemberType]
            model=LLM.MODEL,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an experienced Chief Financial Officer (CFO). "
                        "Generate concise board-level executive summaries."
                    ),
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
        )

        return response["message"]["content"]  # pyright: ignore[reportAny]