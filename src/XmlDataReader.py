# -*- coding: utf-8 -*-
from src.Types import DataType
from src.DataReader import DataReader
import xml.etree.ElementTree as ET


class XmlDataReader(DataReader):
    def __init__(self) -> None:
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        tree = ET.parse(path)
        root = tree.getroot()

        for student_elem in root:
            student_name = student_elem.get("name")
            if not student_name:
                continue
            subjects = []
            for subject_elem in student_elem:
                subject_name = subject_elem.get("name")
                score_text = subject_elem.text
                if not subject_name or not score_text:
                    continue
                try:
                    score = int(score_text.strip())
                except ValueError:
                    continue
                subjects.append((subject_name, score))
            self.students[student_name] = subjects
        return self.students
