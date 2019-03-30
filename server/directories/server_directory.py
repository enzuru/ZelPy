class ServerDirectory:

    objects_by_uuid = {}

    @classmethod
    def add(cls, obj):
        ServerDirectory.objects_by_uuid[obj.uuid] = obj

    @classmethod
    def remove(cls, uuid):
        ServerDirectory.objects_by_uuid.pop(uuid, None)

    @classmethod
    def lookup(cls, uuid):
        if uuid in ServerDirectory.objects_by_uuid:
            return ServerDirectory.objects_by_uuid[uuid]
        else:
            return None

    @classmethod
    def get_objects_by_uuid(cls):
        return ServerDirectory.objects_by_uuid
