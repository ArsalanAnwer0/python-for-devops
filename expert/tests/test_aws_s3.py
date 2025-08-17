import pytest
from expert.aws_s3 import show_all_buckets

class TestShowAllBuckets:
    def test_show_all_buckets_displays_all_bucket_names(self, mocker, capsys):
        bucket_mock1 = mocker.Mock()
        bucket_mock2 = mocker.Mock()
        bucket_mock1.name = "bucket1"
        bucket_mock2.name = "bucket2"
        buckets = [bucket_mock1, bucket_mock2]
        buckets_all_mock = mocker.Mock(return_value=buckets)
        s3_mock = mocker.patch("expert.aws_s3.s3")
        s3_mock.buckets.all = buckets_all_mock

        show_all_buckets()

        captured = capsys.readouterr()
        output_lines = captured.out.strip().split('\n')
        assert output_lines == ["bucket1", "bucket2"]

    def test_show_all_buckets_no_buckets(self, mocker, capsys):
        buckets_all_mock = mocker.Mock(return_value=[])
        s3_mock = mocker.patch("expert.aws_s3.s3")
        s3_mock.buckets.all = buckets_all_mock

        show_all_buckets()

        captured = capsys.readouterr()
        assert captured.out.strip() == ""

    def test_show_all_buckets_prints_names_only(self, mocker, capsys):
        bucket_mock = mocker.Mock()
        bucket_mock.name = "only-name"
        bucket_mock.creation_date = "2022-01-01"
        bucket_mock.extra_field = "unused"
        buckets = [bucket_mock]
        buckets_all_mock = mocker.Mock(return_value=buckets)
        s3_mock = mocker.patch("expert.aws_s3.s3")
        s3_mock.buckets.all = buckets_all_mock

        show_all_buckets()

        captured = capsys.readouterr()
        output = captured.out.strip()
        assert output == "only-name"
        assert "2022-01-01" not in output
        assert "unused" not in output

    def test_show_all_buckets_handles_resource_unavailable(self, mocker):
        buckets_all_mock = mocker.Mock(side_effect=Exception("Resource unavailable"))
        s3_mock = mocker.patch("expert.aws_s3.s3")
        s3_mock.buckets.all = buckets_all_mock

        try:
            show_all_buckets()
        except Exception as exc:
            assert "Resource unavailable" in str(exc)

    def test_show_all_buckets_handles_missing_bucket_name(self, mocker, capsys):
        bucket_mock = mocker.Mock()
        del bucket_mock.name  # Simulate missing name attribute
        buckets = [bucket_mock]
        buckets_all_mock = mocker.Mock(return_value=buckets)
        s3_mock = mocker.patch("expert.aws_s3.s3")
        s3_mock.buckets.all = buckets_all_mock

        try:
            show_all_buckets()
        except AttributeError:
            pass  # Acceptable if function raises on missing attribute

    def test_show_all_buckets_handles_permission_denied(self, mocker):
        import botocore
        error = botocore.exceptions.ClientError(
            error_response={"Error": {"Code": "AccessDenied", "Message": "Access Denied"}},
            operation_name="ListBuckets"
        )
        buckets_all_mock = mocker.Mock(side_effect=error)
        s3_mock = mocker.patch("expert.aws_s3.s3")
        s3_mock.buckets.all = buckets_all_mock

        try:
            show_all_buckets()
        except botocore.exceptions.ClientError as exc:
            assert exc.response['Error']['Code'] == 'AccessDenied'