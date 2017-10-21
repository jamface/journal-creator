"""
Test the doc_generator.
"""
from doc_generator import validate_year, validate_month, create_filename, \
    create_headers, format_day, create_file_content, write_file
import unittest
import shutil
import os


class DocGeneratorTest(unittest.TestCase):
    """
    Test the doc generation function.
    """
    maxDiff = None

    def setUp(self):
        if not os.path.isdir('test'):
            os.mkdir('test')

    def tearDown(self):
        if os.path.isdir('test'):
            shutil.rmtree('test')

    def test_valid_years(self):
        self.assertTrue(validate_year('2016'))
        self.assertTrue(validate_year('2017'))
        self.assertTrue(validate_year('2018'))

    def test_invalid_years(self):
        self.assertFalse(validate_year('jam'))
        self.assertFalse(validate_year(''))
        self.assertFalse(validate_year('1'))
        self.assertFalse(validate_year('3000'))

    def test_valid_months(self):
        for month in TestData.VALID_MONTHS:
            self.assertTrue(validate_month(month))

    def test_invalid_months(self):
        self.assertFalse(validate_year('jam'))
        self.assertFalse(validate_year(''))
        self.assertFalse(validate_year('00'))
        self.assertFalse(validate_year('13'))
        self.assertFalse(validate_year('Aug'))

    def test_create_filename(self):
        self.assertEqual('2016-01 (Jan).md', create_filename('2016', '01'))
        self.assertEqual('2016-02 (Feb).md', create_filename('2016', '02'))
        self.assertEqual('2016-08 (Aug).md', create_filename('2016', '08'))
        self.assertEqual('2016-12 (Dec).md', create_filename('2016', '12'))
        self.assertEqual('2017-03 (Mar).md', create_filename('2017', '03'))
        self.assertEqual('2018-11 (Nov).md', create_filename('2018', '11'))

    def test_format_day(self):
        self.assertEqual('1st', format_day('01'))
        self.assertEqual('2nd', format_day('02'))
        self.assertEqual('3rd', format_day('03'))
        self.assertEqual('4th', format_day('04'))
        self.assertEqual('9th', format_day('09'))
        self.assertEqual('10th', format_day('10'))
        self.assertEqual('11th', format_day('11'))
        self.assertEqual('12th', format_day('12'))
        self.assertEqual('13th', format_day('13'))
        self.assertEqual('20th', format_day('20'))
        self.assertEqual('20th', format_day('20'))
        self.assertEqual('21st', format_day('21'))
        self.assertEqual('22nd', format_day('22'))
        self.assertEqual('23rd', format_day('23'))
        self.assertEqual('24th', format_day('24'))
        self.assertEqual('30th', format_day('30'))
        self.assertEqual('31st', format_day('31'))

    def test_create_headers(self):
        self.assertEqual(TestData.HEADERS_SAMPLE_FEB_16,
                         create_headers('2016', '02'))
        self.assertEqual(TestData.HEADERS_SAMPLE_OCT_18,
                         create_headers('2018', '10'))

    def test_create_file_content(self):
        self.assertEqual(TestData.CONTENT_SAMPLE_FEB_16,
                         create_file_content(TestData.HEADERS_SAMPLE_FEB_16))

    def test_write_file(self):
        success = write_file('2016-02 (Feb).md',
                             TestData.CONTENT_SAMPLE_FEB_16,
                             'test')
        self.assertTrue(success)
        self.assertEqual(['2016-02 (Feb).md'], os.listdir('test'))
        success = write_file('2016-02 (Feb).md',
                             TestData.CONTENT_SAMPLE_FEB_16,
                             'test')
        self.assertFalse(success)


class TestData(object):
    """
    Sample test data to assert Markdown file production
    """
    VALID_MONTHS = ['01', '02', '03', '04', '05', '06',
                    '07', '08', '09', '10', '11', '12']

    HEADERS_SAMPLE_FEB_16 = [
        '# February, 2016',
        '### Monday 29th',
        '### Sunday 28th',
        '### Saturday 27th',
        '### Friday 26th',
        '### Thursday 25th',
        '### Wednesday 24th',
        '### Tuesday 23rd',
        '### Monday 22nd',
        '### Sunday 21st',
        '### Saturday 20th',
        '### Friday 19th',
        '### Thursday 18th',
        '### Wednesday 17th',
        '### Tuesday 16th',
        '### Monday 15th',
        '### Sunday 14th',
        '### Saturday 13th',
        '### Friday 12th',
        '### Thursday 11th',
        '### Wednesday 10th',
        '### Tuesday 9th',
        '### Monday 8th',
        '### Sunday 7th',
        '### Saturday 6th',
        '### Friday 5th',
        '### Thursday 4th',
        '### Wednesday 3rd',
        '### Tuesday 2nd',
        '### Monday 1st'
    ]

    HEADERS_SAMPLE_OCT_18 = [
        '# October, 2018',
        '### Wednesday 31st',
        '### Tuesday 30th',
        '### Monday 29th',
        '### Sunday 28th',
        '### Saturday 27th',
        '### Friday 26th',
        '### Thursday 25th',
        '### Wednesday 24th',
        '### Tuesday 23rd',
        '### Monday 22nd',
        '### Sunday 21st',
        '### Saturday 20th',
        '### Friday 19th',
        '### Thursday 18th',
        '### Wednesday 17th',
        '### Tuesday 16th',
        '### Monday 15th',
        '### Sunday 14th',
        '### Saturday 13th',
        '### Friday 12th',
        '### Thursday 11th',
        '### Wednesday 10th',
        '### Tuesday 9th',
        '### Monday 8th',
        '### Sunday 7th',
        '### Saturday 6th',
        '### Friday 5th',
        '### Thursday 4th',
        '### Wednesday 3rd',
        '### Tuesday 2nd',
        '### Monday 1st'
    ]

    CONTENT_SAMPLE_FEB_16 = \
        ("# February, 2016\n\n### Monday 29th\n\n### Sunday 28th\n\n"
         "### Saturday 27th\n\n### Friday 26th\n\n### Thursday 25th\n\n"
         "### Wednesday 24th\n\n### Tuesday 23rd\n\n### Monday 22nd\n\n"
         "### Sunday 21st\n\n### Saturday 20th\n\n### Friday 19th\n\n"
         "### Thursday 18th\n\n### Wednesday 17th\n\n### Tuesday 16th\n\n"
         "### Monday 15th\n\n### Sunday 14th\n\n### Saturday 13th\n\n"
         "### Friday 12th\n\n### Thursday 11th\n\n### Wednesday 10th\n\n"
         "### Tuesday 9th\n\n### Monday 8th\n\n### Sunday 7th\n\n"
         "### Saturday 6th\n\n### Friday 5th\n\n### Thursday 4th\n\n"
         "### Wednesday 3rd\n\n### Tuesday 2nd\n\n### Monday 1st\n\n")

if __name__ == '__main__':
    unittest.main()
