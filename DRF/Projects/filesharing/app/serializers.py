from jinja2 import FileSystemLoader
from rest_framework import serializers
from .models import Folder,Files
import shutil



class Filelist(serializers.Serializer):
    files = serializers.ListField(child = serializers.FileField(max_length = 10000, allow_empty_file = False, use_url = False))

    def zipper(self, folder):
        shutil.make_archive(f'media/{folder}', 'zip', f'media/{folder}')

    def create(self, validated_data):
        print('three')
        # print('vv',validated_data)
        # vv {'files': [<TemporaryUploadedFile: 1.png (image/png)>, <TemporaryUploadedFile: 000000000000000.png (image/png)>, <TemporaryUploadedFile: 0dfdbb3284aaa8ba7da9079eaccbac3e.jpg (image/jpeg)>]}
        folder = Folder.objects.create()
        files = validated_data.pop('files')
        for f in files:
            Files.objects.create(folder = folder,file=f)
        
        self.zipper(str(folder.uid))
        return {'url':str(folder.uid)}

class GeeksSerializer(serializers.Serializer):

    # initialize fields
    files = serializers.FileField()

    def zipper(self, folder):
        shutil.make_archive(f'media/{folder}', 'zip', f'media/{folder}')

    def create(self, validated_data):
        # print('vv',validated_data)
        # vv {'files': <TemporaryUploadedFile: 0dfdbb3284aaa8ba7da9079eaccbac3e.jpg (image/jpeg)>}
        folder = Folder.objects.create()
        files = validated_data.pop('files')
        Files.objects.create(folder = folder,file=files)
        self.zipper(str(folder.uid))
        return {'url':str(folder.uid)}