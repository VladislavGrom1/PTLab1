# -*- coding: utf-8 -*-
from Types import DataType


class FindBestStudent:
    def __init__(self, data: DataType) -> None:
        self.data: DataType = data

    def find(self) -> str:
        for student, subjects in self.data.items():
            if all(score == 100 for _, score in subjects):
                return f"Студент с 100 баллами по всем дисциплинам: {student}"
        return "Студентов с 100 баллами по всем дисциплинам нет"
