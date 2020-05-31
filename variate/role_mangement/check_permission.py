def check_permission(permission: str, permissions: list):
    for tem_permission in permissions:
        if permission == tem_permission['permission']:
            return True
    return False
