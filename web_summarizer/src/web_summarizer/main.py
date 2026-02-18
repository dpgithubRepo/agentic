#!/usr/bin/env python
import warnings
import time
from web_summarizer.crew import WebSummarizer
import gradio as gr

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def webrun_stream(topic):
    """
    Stream live timer and agent progress while running WebSummarizer.
    """
    start_time = time.time()
    crew = WebSummarizer().crew()

    # Simulated agents (replace with real agent hooks)
    agents = [
        {"name": "Fetching web pages", "status": "working"},
        {"name": "Summarizing content", "status": "pending"},
        {"name": "Finalizing output", "status": "pending"}
    ]

    # Yield updates every second before real crew finishes
    for i in range(len(agents)):
        elapsed = int(time.time() - start_time)
        # Update agent statuses
        for j in range(i + 1):
            agents[j]["status"] = "working"
        for j in range(i + 1, len(agents)):
            agents[j]["status"] = "pending"

        # Build Markdown for agents with colors
        agent_md = "\n".join(
            [f"- { '🟢' if a['status']=='done' else '🔵' if a['status']=='working' else '⚪' } **{a['name']}**"
             for a in agents]
        )

        progress_md = f"""
<div style="font-size:16px; font-weight:bold;">⏳ Loading... {elapsed}s elapsed</div>

**Agents Progress:**
{agent_md}
"""
        yield "", progress_md
        time.sleep(1)

    # Run the real crew workflow
    result_obj = crew.kickoff(inputs={"topic": topic})
    total_time = int(time.time() - start_time)

    # Mark all agents done
    for a in agents:
        a["status"] = "done"
    agent_md = "\n".join([f"- 🟢 **{a['name']}**" for a in agents])

    final_progress = f"""
<div style="font-size:18px; color:green; font-weight:bold;">🎉 Completed in {total_time}s!</div>

**Agents Status:**
{agent_md}
"""

    final_result = f"""
<div style="font-family: Arial, sans-serif;">
<h2 style="color:#1f77b4;">📰 Summarized Result for: {topic}</h2>
<p>{str(result_obj)}</p>
</div>
"""
    yield final_result, final_progress


# Custom CSS for Gradio interface
custom_css = """
body {
    background-color: #f4f6f8;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
h1, h2, h3 {
    color: #1f77b4;
}
.gradio-container {
    max-width: 900px;
    margin: auto;
    padding: 20px;
    background-color: #ffffff;
    border-radius: 15px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.1);
}
.gr-textbox textarea {
    font-size: 16px;
    padding: 10px;
}
.gr-button {
    background-color: #1f77b4 !important;
    color: white !important;
    font-weight: bold;
}
"""

# Gradio interface
interface = gr.Interface(
    fn=webrun_stream,
    inputs=gr.Textbox(
        label="🖊️ Enter a Topic",
        placeholder="E.g., T20 World Cup Australia news"
    ),
    outputs=[
        gr.Markdown(label="📰 Summarized Result"),
        gr.Markdown(label="⏱️ Progress")
    ],
    title="🤖 CREWAI - Agentic Code",
    description="""
Welcome! 🚀 Enter a topic and watch AI agents work in real-time.  
See a **live timer** and the **status of each agent** while your summary is being prepared.
""",
    theme="default",
    css=custom_css
)

if __name__ == "__main__":
    interface.launch()
