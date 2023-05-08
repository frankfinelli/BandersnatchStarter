import altair as alt
from altair import Chart, Tooltip


def chart(df, x, y, target) -> Chart:
    box = alt.Chart(df).mark_boxplot().encode(
        x=x,
        y=y,
        color=target,
        tooltip=Tooltip(df.keys().tolist())
    ).properties(
        width=750,
        height=400,
        background='#C0C0C0',
        padding=6
    )

    return box
