from Duati import DEV_USERS, INSPECTOR, REQUESTER, telethn

IMMUNE_USERS = INSPECTOR.union(REQUESTER).union(DEV_USERS)

IMMUNE_USERS = (
    list(INSPECTOR) + list(REQUESTER) + list(DEV_USERS)
)
