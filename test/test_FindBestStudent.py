# -*- coding: utf-8 -*-
from src.Types import DataType
from src.FindBestStudent import FindBestStudent
import pytest


class TestFindPerfectStudent:
    @pytest.fixture()
    def data_with_best_student(self) -> DataType:
        return {
            "Иванов Иван Иванович": [
                ("математика", 100),
                ("литература", 100),
                ("программирование", 100),
            ],
            "Петров Петр Петрович": [
                ("математика", 90),
                ("химия", 87),
                ("социология", 61),
            ],
        }

    @pytest.fixture()
    def data_without_best_student(self) -> DataType:
        return {
            "Иванов Иван Иванович": [
                ("математика", 99),
                ("физика", 100),
            ],
            "Петров Петр Петрович": [
                ("биология", 100),
                ("география", 95),
            ],
        }

    @pytest.fixture()
    def data_multiple_best_students(self) -> DataType:
        return {
            "Иванов Иван Иванович": [
                ("математика", 100),
                ("литература", 100),
            ],
            "Петров Петр Петрович": [
                ("химия", 100),
                ("биология", 100),
                ("история", 100),
            ],
        }

    def test_find_with_best_student(
        self, data_with_best_student: DataType
    ) -> None:
        finder = FindBestStudent(data_with_best_student)
        result = finder.find()
        assert "Иванов Иван Иванович" in result

    def test_find_without_best_student(
        self, data_without_best_student: DataType
    ) -> None:
        finder = FindBestStudent(data_without_best_student)
        result = finder.find()
        assert result == "Студентов с 100 баллами по всем дисциплинам нет"

    def test_find_multiple_best_students(
        self, data_multiple_best_students: DataType
    ) -> None:
        finder = FindBestStudent(data_multiple_best_students)
        result = finder.find()
        # Возвращает первого студента со всеми 100
        assert "Иванов Иван Иванович" in result
