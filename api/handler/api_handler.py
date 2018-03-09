from api.impl import ActiveSdnServiceImpl


def call_link_flooding_api():
    output = ActiveSdnServiceImpl.findPotentialFloodedLink()
    ActiveSdnServiceImpl.subscribeForStatsFromSwitch([1, 9])
    ActiveSdnServiceImpl.subscribeForLinkFloodingCheck(1, 4, 1)


def handle_event(body):
    if body[0] == 'Link-Flooded':
        call_link_flooding_api()


def action_spec_handler():
    pass


def action_spec_handler():
    pass
