# -*- coding: utf-8 -*-
from Types import DataType
from DataReader import DataReader
import xml.etree.ElementTree as ET


class XmlDataReader(DataReader):
    def __init__(self) -> None:
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        tree = ET.parse(path)
        root = tree.getroot()

        for student_elem in root:
            student_name = student_elem.tag.strip()
            if not student_name:
                continue
            subjects = []
            for subject_elem in student_elem:
                subject_name = subject_elem.tag.strip()
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
