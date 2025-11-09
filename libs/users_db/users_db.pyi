from typing import Optional


type User = tuple[str, str, str]
type UUID = str


class UsersDb:
    def append(self, password: str, email: str, name: str) -> UUID:
        """
        # usage
        USER_DB: UsersDb = UsersDb()

        try:
            return { 'id': USER_DB.append(**my_user) }

        except Exception as e:
            print(e)
        """
        ...

    def discard(self, iden: UUID) -> Optional[UUID]:
        """
        # usage
        USER_DB: UsersDb = UsersDb()

        # def ...
        if ( user_iden := USER_DB.discard('my-uuid-or-public-uuid-from-cookie-jwt-or-anywhere') ):
            return {
                'message': f'User with {user_iden} has removed succesfully'
            }

        raise ValueError('Invalid User Id')
        """
        ...

    def get_by_id(self, iden: UUID) -> Optional[User]:
        """
        # usage
        USER_DB: UsersDb = UsersDb()

        # def ...
        if ( user := USER_DB.get_by_id(my_iden) ):
            return {
                'user': PubUser(**user).json_dumps(),
            }

        raise ValueError('Invalid User Id')
        """
        ...

    def find(self, property: str) -> list[User]:
        """
        # usage
        USER_DB: UsersDb = UsersDb()

        # def ...
        for user in USER_DB.find('name'): # [ ... ] or []
            if user == my_custom_value:
                ...

        raise ValueError('Value not found')
        """
        ...
