import plotly.graph_objects as go
import numpy as np
from plotly.subplots import make_subplots
from pathlib import Path
from typer import Typer

app = Typer(no_args_is_help=True, help="Generate figures for documentation.")


@app.command()
def quadrants():
    # Create a blank figure
    fig = go.Figure()

    # Add horizontal and vertical lines to create the quadrants
    fig.add_hline(y=0, line_width=2, line_dash="dash", line_color="black")
    fig.add_vline(x=0, line_width=2, line_dash="dash", line_color="black")

    # Add semi-transparent shapes for each quadrant
    fig.add_shape(
        type="rect",
        x0=-1,
        x1=0,
        y0=0,
        y1=1,
        fillcolor="rgba(135, 206, 250, 0.3)",
        line_width=0,
    )  # Top-left (Data)
    fig.add_shape(
        type="rect",
        x0=0,
        x1=1,
        y0=0,
        y1=1,
        fillcolor="rgba(144, 238, 144, 0.3)",
        line_width=0,
    )  # Top-right (Modelling)
    fig.add_shape(
        type="rect",
        x0=-1,
        x1=0,
        y0=-1,
        y1=0,
        fillcolor="rgba(255, 182, 193, 0.3)",
        line_width=0,
    )  # Bottom-left (Software)
    fig.add_shape(
        type="rect",
        x0=0,
        x1=1,
        y0=-1,
        y1=0,
        fillcolor="rgba(255, 228, 181, 0.3)",
        line_width=0,
    )  # Bottom-right (Theory)

    # Add annotations for each quadrant with emojis
    fig.add_annotation(
        x=-0.5,
        y=0.5,
        text="📊 Data",
        showarrow=False,
        font=dict(size=40, color="blue", family="Arial Black"),
    )
    fig.add_annotation(
        x=0.5,
        y=0.5,
        text="🧠 Modelling",
        showarrow=False,
        font=dict(size=40, color="green", family="Arial Black"),
    )
    fig.add_annotation(
        x=-0.5,
        y=-0.5,
        text="💻 Software",
        showarrow=False,
        font=dict(size=40, color="red", family="Arial Black"),
    )
    fig.add_annotation(
        x=0.5,
        y=-0.5,
        text="📚 Theory",
        showarrow=False,
        font=dict(size=40, color="orange", family="Arial Black"),
    )

    # Add a title to the figure
    fig.update_layout(
        xaxis=dict(range=[-1.0, 1.0], zeroline=False, showticklabels=False),
        yaxis=dict(range=[-1.0, 1.0], zeroline=False, showticklabels=False),
        width=700,
        height=700,
        margin=dict(l=20, r=20, t=50, b=20),  # Adjust margins
    )

    # Export the figure to a PNG file
    output_path = Path("docs/figures/quadrants.png")
    output_path.parent.mkdir(parents=True, exist_ok=True)  # Ensure directory exists
    fig.write_image(output_path)


@app.command()
def grade_distribution():
    grade = [-3, 0, 2, 4, 7, 10, 12]
    count = [0, 1, 2, 2, 4, 16, 31]

    # Calculate total count and percentages
    total_count = sum(count)
    percentage = [(c / total_count) * 100 for c in count]

    # Create figure with bar labels
    fig = go.Figure(
        data=[
            go.Bar(
                x=grade,
                y=percentage,
                text=[f"{p:.1f}%" for p in percentage],
                textposition="outside",  # Show text above bars
                marker=dict(color="royalblue"),  # Adjust bar color
            )
        ]
    )

    fig.update_layout(
        title="Grade Distribution",
        title_font_size=24,
        xaxis_title="Grade",
        yaxis_title="Percentage",
        font=dict(size=18),
        xaxis=dict(tickfont=dict(size=14), tickvals=grade),
        yaxis=dict(
            tickfont=dict(size=14),
            tickformat=".1f%",  # Format y-axis as percentage
            range=[0, max(percentage) * 1.2],
        ),
        bargap=0.05,  # Reduce whitespace between bars
        margin=dict(t=80),
    )

    output_path = Path("docs/figures/grade_distribution.png")
    output_path.parent.mkdir(parents=True, exist_ok=True)  # Ensure directory exists
    fig.write_image(output_path)


@app.command()
def student_writing():
    # Time values from 0 to 1
    time = np.linspace(0, 1, 100)

    # Define the progress curves
    bad_student_progress = 1 / (1 + np.exp(-25 * (time - 0.90)))
    good_student_progress = 1 / (1 + np.exp(-15 * (time - 0.6)))

    # Create figure with secondary y-axis for stress level
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    # Add progress curves
    fig.add_trace(
        go.Scatter(
            x=time,
            y=bad_student_progress,
            mode="lines",
            name="Bad Student (Last Minute)",
            line=dict(color="#FF6B6B", width=4),
            hovertemplate="<b>Bad Student</b><br>Time: %{x:.1%}<br>Progress: %{y:.1%}<extra></extra>",
        ),
        secondary_y=False,
    )

    fig.add_trace(
        go.Scatter(
            x=time,
            y=good_student_progress,
            mode="lines",
            name="Good Student (Gradual)",
            line=dict(color="#4ECDC4", width=4),
            hovertemplate="<b>Good Student</b><br>Time: %{x:.1%}<br>Progress: %{y:.1%}<extra></extra>",
        ),
        secondary_y=False,
    )

    # Add shapes and annotations (same as above)
    fig.add_shape(
        type="line",
        x0=1.0,
        y0=0,
        x1=1.0,
        y1=1,
        line=dict(color="red", width=2, dash="dash"),
    )
    fig.add_shape(
        type="rect",
        x0=0.8,
        y0=0,
        x1=1.0,
        y1=1,
        fillcolor="red",
        opacity=0.1,
        line_width=0,
    )

    # Update layout
    fig.update_layout(
        title=dict(
            text="<b>Report Writing Progress Over Time</b>",
            x=0.5,
            font=dict(size=22, family="Arial"),
        ),
        xaxis=dict(
            title="Time",
            range=[0, 1],
            dtick=0.2,
            tickformat=",.0%",
            gridcolor="lightgray",
        ),
        yaxis=dict(
            title="Progress",
            range=[0, 1],
            dtick=0.2,
            tickformat=",.0%",
            gridcolor="lightgray",
        ),
        plot_bgcolor="white",
        paper_bgcolor="white",
        legend=dict(
            x=0.02,
            y=0.98,
            bgcolor="rgba(255,255,255,0.9)",
            bordercolor="lightgray",
            borderwidth=1,
        ),
        width=900,
        height=600,
    )

    # Add annotations (same annotations as previous version)
    annotations = [
        dict(
            x=0.97,
            y=0.1,
            text="DEADLINE",
            showarrow=False,
            textangle=-90,
            font=dict(color="red", size=12, weight="bold"),
            bgcolor="white",
        ),
        dict(
            x=0.9,
            y=0.5,
            text="PANIC ZONE",
            showarrow=False,
            textangle=-90,
            font=dict(color="red", size=14, weight="bold"),
            bgcolor="white",
        ),
        dict(
            x=0.3,
            y=0.7,
            text="Steady Progress",
            showarrow=False,
            font=dict(color="#2E8B57", size=12, weight="bold"),
            bgcolor="white",
        ),
        dict(
            x=0.88,
            y=0.2,
            text="Last Minute Rush!",
            showarrow=True,
            arrowhead=2,
            ax=50,
            ay=-30,
            font=dict(color="#FF6B6B", size=12, weight="bold"),
            bgcolor="white",
        ),
    ]

    for annotation in annotations:
        fig.add_annotation(annotation)

    output_path = Path("docs/figures/student_writing.png")
    output_path.parent.mkdir(parents=True, exist_ok=True)  # Ensure directory exists
    fig.write_image(output_path)


@app.command()
def all():
    print("Quadrant fig...")
    quadrants()
    print("Grade distribution fig...")
    grade_distribution()
    print("Student writing fig...")
    student_writing()


if __name__ == "__main__":
    app()
