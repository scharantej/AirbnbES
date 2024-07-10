## Flask Application Design for an Airbnb Clone for the Spanish Market

### HTML Files

1. **home.html**: Main landing page, showcasing available properties, search bar, and user dashboard.
2. **property_detail.html**: Detailed page for each property, including photos, amenities, availability, and booking options.
3. **user_dashboard.html**: Personal area for users, allowing them to manage bookings, update profiles, and send messages.
4. **host_dashboard.html**: Dedicated section for property owners to manage their listings, bookings, and communication with guests.
5. **search_results.html**: Page displaying search results based on user criteria, with filter options and sorting capabilities.

### Routes

1. **home**:
   - Purpose: Displays the main landing page.
   - Method: GET
   - URL: `/`
2. **search**:
   - Purpose: Processes search queries and redirects to search results page.
   - Method: POST
   - URL: `/search`
3. **property_detail/:id**:
   - Purpose: Shows the detailed information of a specific property.
   - Method: GET
   - URL: `/property_detail/<int:id>`
4. **book/:property_id**:
   - Purpose: Initiates the booking process for a property.
   - Method: POST
   - URL: `/book/<int:property_id>`
5. **user_dashboard**:
   - Purpose: Redirects to the user's dashboard page.
   - Method: GET
   - URL: `/user_dashboard`
6. **host_dashboard**:
   - Purpose: Redirects to the host's dashboard page.
   - Method: GET
   - URL: `/host_dashboard`
7. **login**:
   - Purpose: Handles user login.
   - Method: POST
   - URL: `/login`
8. **logout**:
   - Purpose: Logs out the user.
   - Method: GET
   - URL: `/logout`