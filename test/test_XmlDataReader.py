# -*- coding: utf-8 -*-
import pytest
from src.Types import DataType
from src.XmlDataReader import XmlDataReader


class TestXmlDataReader:
    @pytest.fixture()
    def xml_content_and_data(self) -> tuple[str, DataType]:
        xml_content = (
            '<?xml version="1.0" encoding="UTF-8"?>\n'
            '<root>\n'
            '  <student name="Иванов Иван Иванович">\n'
            '    <subject name="математика">67</subject>\n'
            '    <subject name="литература">100</subject>\n'
            '    <subject name="программирование">91</subject>\n'
            '  </student>\n'
            '  <student name="Петров Петр Петрович">\n'
            '    <subject name="математика">78</subject>\n'
            '    <subject name="химия">87</subject>\n'
            '    <subject name="социология">61</subject>\n'
            '  </student>\n'
            '</root>\n'
        )
        expected_data: DataType = {
            "Иванов Иван Иванович": [
                ("математика", 67),
                ("литература", 100),
                ("программирование", 91)
            ],
            "Петров Петр Петрович": [
                ("математика", 78),
                ("химия", 87),
                ("социология", 61)
            ]
        }
        return xml_content, expected_data

    @pytest.fixture()
    def xml_filepath_and_data(
        self,
        xml_content_and_data: tuple[str, DataType],
        tmpdir
    ) -> tuple[str, DataType]:
        p = tmpdir.mkdir("xmldatadir").join("students.xml")
        p.write_text(xml_content_and_data[0], encoding='utf-8')
        return str(p), xml_content_and_data[1]

    def test_read(
        self, xml_filepath_and_data: tuple[str, DataType]
    ) -> None:
        reader = XmlDataReader()
        parsed_data = reader.read(xml_filepath_and_data[0])
        assert parsed_data == xml_filepath_and_data[1]
