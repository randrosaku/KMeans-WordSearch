from pydantic import BaseModel, FilePath, validator


class InputModel(BaseModel):
    file: FilePath
    word: str

    @validator("file")
    def check_txt(cls, value):
        if not str(value).endswith(".txt"):
            raise ValueError("The file must be a .txt file.")
        return value
