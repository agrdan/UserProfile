from main import db
from datasource.changelog.changelog import ChangeLog as cl
from datasource.entity.UserType import UserType
from datasource.entity.User import User


class InitializeService:

    def __init__(self):
        pass

    @staticmethod
    def initialize():
        db.create_all()

        # user_type
        type_admin = UserType()
        type_admin.type = 1
        type_admin.name = 'ADMIN'
        type_normal = UserType()
        type_normal.type = 2
        type_normal.name = 'USER'

        type_superadmin = UserType()
        type_superadmin.type = 3
        type_superadmin.name = 'SUPERADMIN'
        cl.add_params('user_type-1', type_admin, type_normal)
        cl.add_params('user_type-2', type_superadmin)
        """
        
        brada = User().create("agrdan", "!Lunarstrain123!", "Andreas", "Grđan", 1)
        print(brada)

        admin = User().create("admin", "Admin2020!", "admin", "admin", 3)

        cl.add_params('user-1', brada)
        cl.add_params('user-2', admin)
        """
