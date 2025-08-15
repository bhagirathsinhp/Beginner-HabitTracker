# 🏋️‍♂️ Pixela Workout Tracker

A Python automation project that logs **daily workout hours** to a visual graph using the [Pixela API](https://pixe.la/).  
This script lets you:
- Create a Pixela user account
- Create and edit a workout graph
- Post daily workout logs
- Optionally delete logs

---

## 📌 What is Pixela?
Pixela is a free web service that lets you create visual habit-tracking graphs just by calling an API. This project uses it to track gym/workout time.

---

## 🚀 Features

- ✅ Create a Pixela user account (only once)
- 📊 Create a graph for daily workout tracking
- 📝 Log daily workout hours as "pixels" on the graph
- ✏️ Edit graph details
- ❌ Delete a workout log (optional)
- 🔐 Uses `.env` file for secure storage of API keys and credentials

---

## 🛠️ Technologies Used

- Python 3
- `requests` — For making API calls
- `dotenv` — For environment variable management
- Pixela API — For graph creation and data logging

---

## 📂 Project Structure

    pixela-workout-tracker/
    │
    ├── main.py           # Main Python script
    ├── .env              # Environment variables (API keys, usernames, etc.)
    └── README.md         # Project documentation

---

## 🔑 Environment Variables

- Create a .env file in the project root with:

      PIXELA_ENDPOINT=https://pixe.la/v1/users
      API_TOKEN=your_pixela_api_token
      USER_NAME=your_pixela_username
      GRAPH_ID=your_graph_id

---

## ▶️ How to Use

<ol>
  <li>Install dependencies:</li>
            
    pip install requests python-dotenv

  <li>Set up your .env file with your Pixela credentials</li>
  <li>Run the script:</li>

      python main.py
  
  <li>Input your workout hours when prompted:</li>

    How many hours did you workout today?: 1.5
  
</ol> 

---

## 📜 Example Workflow

1. (Optional, first time only) Create a Pixela user:

       create_user_request = requests.post(url=PIXELA_ENDPOINT, json=create_user_params)

2. Create a workout graph:

        graph_request = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=graph_header)

3. Log your daily workout hours:

        post_pixel = requests.post(url=GRAPH_ID_ENDPOINT, json=pixel_data, headers=graph_header)

4. (Optional) Delete today’s pixel:

        requests.delete(url=f'{GRAPH_ID_ENDPOINT}/{today}', headers=graph_header)

---




