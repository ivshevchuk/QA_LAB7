import json


def parser(iperf_result):
    return list(map(lambda interval: parse_interval(interval), json.loads(iperf_result.stdout)["intervals"]))


def parse_interval(interval):
    intervalSum = interval["sum"]
    return {
        "Interval": f"{intervalSum['start']:.{1}f}-{intervalSum['end']:.{1}f}",
        "Transfer": float(f"{intervalSum['bytes']:.{1}f}"),
        "Transfer_unit": "Bytes",
        "Bandwidth": float(f"{intervalSum['bits_per_second']:.{1}f}"),
        "Bandwidth_unit": "Bits/sec"
    }
