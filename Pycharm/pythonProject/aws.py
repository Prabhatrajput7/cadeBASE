d = {
    'Reservations': [
        {
            'Groups': [
                {
                    'GroupName': 'string',
                    'GroupId': 'string'
                },
            ],
            'Instances': [
                {
                    'AmiLaunchIndex': 123,
                    'ImageId': 'string',
                    'Monitoring': [{
                        'State': 'disabled'
                    }],
                    'Placement': {
                        'AvailabilityZone': 'string',
                        'Affinity': 'string',
                        'GroupName': 'string'
                    },
                    'Platform': 'Windows',
                    'ProductCodes': [
                        {
                            'ProductCodeId': 'string',
                            'ProductCodeType': 'devpay'
                        },
                    ],
                    'PublicDnsName': 'string',
                    'PublicIpAddress': 'string',
                    'RamdiskId': 'string',
                    'State': {
                        'Code': 123,
                        'Name': 'pending'
                    },
                },
            ],
            'OwnerId': 'string',
            'RequesterId': 'string',
            'ReservationId': 'string'
        },
    ],
    'NextToken': 'string'
}

import pprint
for i in d['Reservations']:
    for j in i['Instances']:
        for k in j['Monitoring']:
            print(k['State'])
# print(d['Reservations'][0]['Groups'][0]['GroupName'])
# for i in d['Reservations']:
#     for j in i['Instances']:
#         print(j)


# for i in d['Reservations']:
#     print(i)
