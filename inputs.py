import jsonpickle
class AdRequest:
    def __init__(self):
        self.request_id = None
        self.user_id = None
        self.session_id = None
        self.timestamp = None
        self.device_type = None
        self.os_name = None
        self.browser_version = None
        self.ip_address = None
        self.country = None
        self.region = None
        self.city = None
        self.zip_code = None
        self.latitude = None
        self.longitude = None
        self.page_url = None

    def to_json(self):
        return jsonpickle.encode(self, unpicklable=False)

class AdResponse:
    def __init__(self):
        self.response_id = None
        self.request_id = None  # Common field to join with AdRequest
        self.user_id = None     # Common field
        self.session_id = None  # Common field
        self.timestamp = None
        self.ad_ids = None      # List of ad identifiers
        self.campaign_ids = None
        self.advertiser_ids = None
        self.ad_types = None
        self.bidding_costs = None
        self.currency = None
        self.creative_urls = None
        self.destination_urls = None
        self.ad_sizes = None
        self.display_times = None
    def to_json(self):
        return jsonpickle.encode(self, unpicklable=False)

class AdClick:
    def __init__(self):
        self.click_id = None
        self.response_id = None  # Common field to join with AdResponse
        self.request_id = None   # Common field to join with AdRequest
        self.user_id = None      # Common field
        self.session_id = None   # Common field
        self.timestamp = None
        self.clicked_ad_id = None
        self.campaign_id = None
        self.advertiser_id = None
        self.click_position = None
        self.referrer_url = None
        self.exit_url = None
        self.time_spent = None
        self.is_converted = None
        self.conversion_details = None
    def to_json(self):
        return jsonpickle.encode(self, unpicklable=False)