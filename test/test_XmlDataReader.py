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
            '  <Иванов Иван Иванович>\n'
            '    <математика>67</математика>\n'
            '    <литература>100</литература>\n'
            '    <программирование>91</программирование>\n'
            '  </Иванов Иван Иванович>\n'
            '  <Петров Петр Петрович>\n'
            '    <математика>78</математика>\n'
            '    <химия>87</химия>\n'
            '    <социология>61</социология>\n'
            '  </Петров Петр Петрович>\n'
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
