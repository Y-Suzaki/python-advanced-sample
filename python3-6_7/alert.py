import copy
import json
from typing import List


class AlertEvent:
    def __init__(self, alert_event_list):
        self._alert_list: List[dict] = copy.deepcopy(alert_event_list)
        for alert in self._alert_list:
            alert['event_type'] = 'option' if alert['event_type'] == 1 else 'crash'

    def filter_latest_alert(self):
        _alert_list = []
        for alert in self._alert_list:
            _alert_list.append(alert)
        self._alert_list = _alert_list
        return self

    def merge_device_label(self, device_list: List[dict]):
        return self._merge_device(device_list, 'label')

    def merge_device_type(self, device_list: List[dict]):
        return self._merge_device(device_list, 'device_type')

    def _merge_device(self, device_list: List[dict], key: str):
        _alert_list = []
        for alert in self._alert_list:
            device = next(filter(lambda x: x['imei'] == alert['imei'], device_list), None)
            if device is None:
                raise Exception('')
            alert[key] = device[key]
        return self

    def sort_by_date_time(self):
        self._alert_list.sort(key=lambda x: x['label'], reverse=True)
        return self

    def to_list(self):
        return self._alert_list


__alert_event = [
    {
        'event_id': 1,
        'event_type': 1,
        'imei': 'a0001'
    },
    {
        'event_id': 2,
        'event_type': 2,
        'imei': 'b0001'
    }
]

__device_list_1 = [
    {
        'imei': 'a0001',
        'label': 'label-1'
    },
    {
        'imei': 'b0001',
        'label': 'label-2'
    }
]

__device_list_2 = [
    {
        'imei': 'a0001',
        'device_type': 'type-1'
    },
    {
        'imei': 'b0001',
        'device_type': 'type-2'
    }
]

alert_list = (
    AlertEvent(__alert_event)
    .filter_latest_alert()
    .merge_device_label(__device_list_1).merge_device_type(__device_list_2)
    .sort_by_date_time()
    .to_list()
)

print(json.dumps(alert_list, indent=4))
