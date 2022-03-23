import io
import unittest
from unittest.mock import patch
from textwrap import dedent

from code2img.utils import parse_str, read_file, split_path, job_done


class TestCarbonPyUtils(unittest.TestCase):

    def test_job_done(self):
        data = "file"
        expected = dedent("""\
            Done!
            Image created in current directory: file.png\n
            """
        )  # noqa: E124
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            job_done(data)
            self.assertEqual(mock_stdout.getvalue(), expected)

    def test_split_path(self):
        NotImplementedError()

    def test_read_file(self):
        NotImplementedError()

    def test_parse_str(self):
        NotImplementedError()


if __name__ == '__main__':
    unittest.main()