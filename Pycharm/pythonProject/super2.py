# class ClientLocator:
#     def __init__(self, client):
#         self._client = client
#
#     def get_client(self):
#         return self._client
#
#
# class EC2Client(ClientLocator):
#     def __init__(self):
#         super().__init__('ec2')
#
# e =EC2Client()
# print(e.get_client())
