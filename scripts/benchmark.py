from locust import HttpUser, task, TaskSet, between

class SimpleTaskSet(TaskSet):
    @task
    def entrance(self):
        headers = {
            "Accept": "application/json",
            "Anonymous-Id": "ckhco6yjw00005t5fzo72z5ee",
            "Authorization": "Basic bWFtaWxvdmU6aWxvdmV1cG4=",
            "X-OAuth-Token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImJjZjU1ZTViNGYyN2UyYzhmZGExMzA3YTA0ODAzMTc2MTlkZDA4Mjc2NTYwNDk0MzVlYTc4NTRiMTc2NDdiMTZkZDZkOTVlOTUzMTA2MWEwIn0.eyJwbGF0Zm9ybSI6ImRlc2t0b3AiLCJhdWQiOiIxIiwianRpIjoiYmNmNTVlNWI0ZjI3ZTJjOGZkYTEzMDdhMDQ4MDMxNzYxOWRkMDgyNzY1NjA0OTQzNWVhNzg1NGIxNzY0N2IxNmRkNmQ5NWU5NTMxMDYxYTAiLCJpYXQiOjE2NzAzOTU5ODcsIm5iZiI6MTY3MDM5NTk4NywiZXhwIjoxNjcyOTg3OTg2LCJzdWIiOiI2NTM5MDMiLCJzY29wZXMiOltdfQ.gp-1MnVvOhhoFQ1r_M89lRR0_wPkBdBsuM0KjnfcYO3X7VUck7oRw3XH9bWF9K3pP9lpyGStl0zEhrti-ZgRVU5F6vUgyJbgtKDnHXOFIvjQcdB7ME6S3vdyF_YVfSZF4KyZe_i5glrm94uqevwtgwBM3_9eVzVLsXS-Wng2AAZjYeX2pLMUR05pC2vhIvfTwHIOIP5TV3DyzUrI3vZ4OSNYaPaXQiI7B4KzUjo8OEe3auAiatvhfB4bC7daLQz-3obDpz9JhaiTdDZBYuJCFsU0gbhCZ0fFRPbt3n0Ieh0bpIbnVfWCOB5RA3YdF06O-dPfolnjj7XHcuBH8MYkbLNTmhZ-oi8V-q6Wms79ymRoFxflWbDgzM2Pd0FNVNcQWHcxuYBLxkVd55ZROzt8mklDjWPz2S8POlCbYlnyJzpMuyWVXgNDLfDpc9CruBv4cZxE5Ijt-3GnENoDoeHDSCowovwxFtIQLv0eTrmg-nZt-b4MZtoGfyKBSiNPbvFE4ILBGrzC0GrWZFeSAvvXiR5O-rVkltG6_UN_AnqyFUdkifNVIGKjxGVNoYtnxXEvcma5nCOC1oaQBOzGWfQ9DGSQH9WZkvxz47B0rk-9jzrQizHDGTFO1_dblS0_X7-26h2qzucOyQlo-wE1zIXJxJX-cCka794RI9C_EEaZ__M",
            "Device-Type": "ios"
        }
        data = {
            "device_id": "ckhco6yjw00005t5fzo72z5ee",
            "user_id": "653903",
            "send_id": "ckhk97cm800005t5f1p2lo0jp",
            "client_send_at": "1670402560000",
            "query_string": "utm_source=google&utm_medium=cps&utm_campaign=1116_OATimeline_6395&utm_content=gb"
        }
        self.client.post('/tracking/entrance', json = data, headers = headers)

class Benchmark(HttpUser):
    tasks = [SimpleTaskSet]
    wait_time = between(1, 5)
