import pytest
import parser


class TestSuite:

    @pytest.mark.usefixtures("server")
    def test_iperf3_client_connection(self, client):
     pars = parser.parser(client)
     assert len(pars)!=0
     for value in parser.parser(client):
      print(value)
      assert value["Transfer"] > 2000000 and value["Bandwidth"] > 20000000
