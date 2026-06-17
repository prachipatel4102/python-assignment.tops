#Q1  Create a Python dictionary called insta_followers that stores the number of followers for 5 Instagram influencers (use their usernames as keys and follower counts as values). Print the dictionary
insta_followers = {
    "virat18": 270000000,
    "shraddhakapoor": 95000000,
    "aliaabhatt": 87000000,
    "carryminati": 21000000,
    "varun dhawan": 45300000
}
print(insta_followers)

#Q2 Add a new influencer to your insta_followers dictionary and update the follower count for one existing influencer. Then, delete one influencer from the dictionary and print the updated dictionary.
insta_followers = {
    "virat18": 270000000,
    "shraddhakapoor": 95000000,
    "aliaabhatt": 87000000,
    "carryminati": 21000000,
    "varun dhawan": 45300000
}
insta_followers["Mrbeast"]=65000000
insta_followers["carryminati"]=22000000
del insta_followers["varun dhawan"]
print(insta_followers)

#Q3 Given a dictionary called food_prices with 5 Zomato food items as keys and their prices as values, write code to display all items that cost more than ₹200.
food_prices={
    "pizza":250,
    "burger":300,
    "garlic braed":150,
    "sandwich":150,
    "biryani":300
}
for item,price in food_prices.items():
    if price>200:
        print(item,":",price)

#Q4 Create two sets: flipkart_users and myntra_users, each containing 5 unique usernames. Find and print the set of users who have accounts on both platforms using set intersection.
flipkart_users={"prachi","manya","jimit","vrushti","rohan"}
myntra_users={"prachi","jimit","swara","manya","niv"}
common_user= flipkart_users.intersection(myntra_users)
print(common_user)

#Q5 Write a function get_unique_artists(spotify_playlist1, spotify_playlist2) that takes two sets of artist names and returns a set of all unique artists across both playlists (set union).<br><br><em><strong>Hint:</strong> Use the union() method or the | operator for sets.</em>
def get_unique_artists(spotify_playlist1,spotify_playlist2):
    return spotify_playlist1.union(spotify_playlist2)

playlist1={"arijit singh","armaan malik","atif aslam"}
playlist2={"arijit singh","neha kakkar","darshan raval"}
result=get_unique_artists(playlist1,playlist2)
print(result)