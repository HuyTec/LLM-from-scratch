"""Encode and decode text with a character vocabulary."""

# TODO: Build a deterministic vocabulary from train text and reserve <unk>.
import json

class CharTokenizer:
    def __init__(self, chars, unk_token="<unk>"):
        self.unk_token = unk_token
        self.itos = [unk_token] + sorted(chars)   # id -> ký tự
        self.stoi = {c: i for i, c in enumerate(self.itos)}  # ký tự -> id

    def encode(self, text):
        # TODO: đổi từng ký tự thành id, ký tự lạ thì dùng id của <unk>
        ...

    def decode(self, ids):
        # TODO: đổi id về ký tự rồi ghép thành chuỗi
        ...

    def save(self, path):
        with open(path, "w", encoding="utf-8") as f:
            json.dump(self.itos, f, ensure_ascii=False)

    @classmethod
    def load(cls, path):
        with open(path, encoding="utf-8") as f:
            itos = json.load(f)
        tok = cls([])
        tok.itos = itos
        tok.stoi = {c: i for i, c in enumerate(itos)}
        return tok