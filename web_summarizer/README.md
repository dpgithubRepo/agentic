🤖 CREWAI - Agentic Dashboard

A live AI agent dashboard built with Gradio that demonstrates Crewai agents working in real-time to summarize web topics. This project streams agent progress and a live timer while the summarization workflow executes, giving users a professional, dashboard-like experience.

<img width="886" height="866" alt="image" src="https://github.com/user-attachments/assets/052225a6-0f4b-4cf1-ac10-b57207b82272" />


📝 Features

Live Timer: Shows elapsed time while the AI agents are working.

Agent Progress: Displays the status of each agent with intuitive colored icons:

🔵 Working

⚪ Pending

🟢 Done

Real-Time Streaming: Results update dynamically as the workflow progresses.

Beautiful Interface:

Modern card layout with rounded corners and shadow.

Custom fonts, colors, and styled Markdown.

Professional, responsive design.

Easy Input: Users simply enter a topic and watch the agents work.

⚡ Demo

When a user enters a topic, the interface shows:

A live timer updating every second.

Agent progress in Markdown with emojis.

Summarized result displayed in a styled, readable format.

🛠️ Installation

Clone the repository:

git clone https://github.com/yourusername/crewai-dashboard.git
cd crewai-dashboard


Create a virtual environment (recommended):

python -m venv .venv
source .venv/bin/activate    # On Windows: .venv\Scripts\activate


Install dependencies:

pip install -r requirements.txt


Dependencies include:

gradio – for the interface

web_summarizer – for Crewai workflow execution

🚀 Usage

Run the dashboard locally:

python main.py


Open the link displayed in your terminal (e.g., http://127.0.0.1:7860).

Enter a topic in the input box.

Watch live timer and agents progress while the summary is being generated.

🎨 Customization

CSS Styling: Modify the custom_css in main.py to change fonts, colors, or layout.

Agents: Replace simulated agent steps with real Crewai agent hooks.

Timer Format: Customize the timer display in webrun_stream for MM:SS format or progress bars.

📂 Project Structure
crewai-dashboard/
│
├── main.py           # Main Gradio interface and workflow
├── requirements.txt  # Python dependencies
├── README.md         # This file
└── web_summarizer/   # Crewai summarizer module

💡 Future Enhancements

Add real-time progress bars for each agent.

Integrate live streaming of agent logs for full transparency.

Deploy to Heroku / AWS / Streamlit Cloud for online access.

Include analytics dashboard showing multiple topics and agent performance.

⚖️ License

This project is licensed under the MIT License – see LICENSE
 for details.

👨‍💻 Author

Durga Prasad 
📧 Email: durga.pras10@gmail.com

💻 [GitHub:](https://github.com/dpgithubRepo)
