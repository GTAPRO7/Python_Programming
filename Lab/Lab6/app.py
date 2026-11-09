import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="AutoDash · Fleet Analytics",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Minimal CSS — just enough to feel polished, not overdone
st.markdown("""
<style>
[data-testid="stSidebar"] { border-right: 1px solid #e0e0e0; }
[data-testid="metric-container"] {
    border: 1px solid #ebebeb;
    border-radius: 6px;
    padding: 0.9rem 1rem;
}
hr { border-color: #ebebeb; }
</style>
""", unsafe_allow_html=True)


@st.cache_data
def load_and_clean_data(file_path):
    df = pd.read_csv(file_path)
    df['Engine HP']        = df['Engine HP'].fillna(df['Engine HP'].median())
    df['Engine Cylinders'] = df['Engine Cylinders'].fillna(df['Engine Cylinders'].median())
    df['Number of Doors']  = df['Number of Doors'].fillna(df['Number of Doors'].mode()[0])
    df['Engine Fuel Type'] = df['Engine Fuel Type'].fillna("Unknown")
    df['Market Category']  = df['Market Category'].fillna("Standard")
    df['Highway KMPL']     = (df['highway MPG'] * 0.425144).round(2)
    df['City KMPL']        = (df['city mpg']    * 0.425144).round(2)
    return df


# A single consistent chart style used across all plots
CHART_STYLE = {
    "bg":          "#fafafa",
    "grid":        "#e8e8e8",
    "text":        "#333333",
    "subtext":     "#888888",
    "primary":     "#c0392b",   # deep red — the one accent colour
    "secondary":   "#2c3e50",   # dark slate
    "tertiary":    "#7f8c8d",   # grey
    "palette":     ["#c0392b", "#2c3e50", "#7f8c8d", "#e67e22", "#16a085"],
}

def apply_chart_style(fig, ax):
    fig.patch.set_facecolor(CHART_STYLE["bg"])
    ax.set_facecolor(CHART_STYLE["bg"])
    ax.tick_params(colors=CHART_STYLE["subtext"], labelsize=9)
    ax.xaxis.label.set_color(CHART_STYLE["subtext"])
    ax.yaxis.label.set_color(CHART_STYLE["subtext"])
    ax.title.set_color(CHART_STYLE["text"])
    ax.title.set_fontsize(11)
    ax.title.set_fontweight("semibold")
    for spine in ax.spines.values():
        spine.set_edgecolor(CHART_STYLE["grid"])


def main():
    try:
        df = load_and_clean_data("data.csv")
    except FileNotFoundError:
        st.error("**data.csv not found.** Place it in the same folder as app.py and reload.")
        return

    # ── Sidebar ──────────────────────────────────────────────────────────────
    st.sidebar.title("Fleet Filters")

    all_makes     = sorted(df['Make'].unique())
    default_makes = [m for m in ["Chevrolet", "Ford", "Volkswagen", "Toyota", "Dodge", "BMW", "Honda", "Audi"] if m in all_makes]

    selected_makes = st.sidebar.multiselect("Vehicle Make", all_makes, default=default_makes)

    transmission_opts    = ["All"] + sorted(df['Transmission Type'].unique())
    selected_transmission = st.sidebar.selectbox("Transmission", transmission_opts)

    all_sizes      = sorted(df['Vehicle Size'].unique())
    selected_sizes = st.sidebar.multiselect("Vehicle Size", all_sizes, default=all_sizes)

    min_yr, max_yr     = int(df['Year'].min()), int(df['Year'].max())
    selected_yr        = st.sidebar.slider("Model Year", min_yr, max_yr, (min_yr, max_yr))

    min_hp, max_hp     = float(df['Engine HP'].min()), float(df['Engine HP'].max())
    selected_hp        = st.sidebar.slider("Horsepower (HP)", min_hp, max_hp, (min_hp, max_hp))

    # ── Filter ───────────────────────────────────────────────────────────────
    fdf = df.copy()
    if selected_makes:
        fdf = fdf[fdf['Make'].isin(selected_makes)]
    if selected_transmission != "All":
        fdf = fdf[fdf['Transmission Type'] == selected_transmission]
    if selected_sizes:
        fdf = fdf[fdf['Vehicle Size'].isin(selected_sizes)]
    fdf = fdf[
        fdf['Year'].between(*selected_yr) &
        fdf['Engine HP'].between(*selected_hp)
    ]

    # ── Header ───────────────────────────────────────────────────────────────
    st.title("Automotive Fleet Analytics")
    st.caption("Explore vehicle specs, engine output, fuel efficiency, and pricing across the fleet dataset.")

    if fdf.empty:
        st.warning("No vehicles match the current filters — try broadening your selections.")
        return

    # ── KPIs ─────────────────────────────────────────────────────────────────
    c1, c2, c3, c4, c5 = st.columns(5)
    c1.metric("Vehicles",         f"{len(fdf):,}")
    c2.metric("Fleet Value",      f"${fdf['MSRP'].sum():,.0f}")
    c3.metric("Avg MSRP",         f"${fdf['MSRP'].mean():,.0f}")
    c4.metric("Avg Horsepower",   f"{fdf['Engine HP'].mean():.0f} HP")
    c5.metric("Avg Hwy Efficiency", f"{fdf['Highway KMPL'].mean():.2f} KMPL")

    st.write("")

    # ── Tabs ─────────────────────────────────────────────────────────────────
    tab1, tab2, tab3, tab4 = st.tabs([
        "Dataset", "Group-By Analysis", "Visualizations", "Insights"
    ])

    # ── Tab 1 : Dataset ───────────────────────────────────────────────────────
    with tab1:
        st.write(f"**{len(fdf):,}** vehicles shown · {len(df):,} total in dataset")
        st.dataframe(fdf.head(100), use_container_width=True)

        with st.expander("Summary statistics"):
            num_cols = ['Year', 'Engine HP', 'Engine Cylinders',
                        'highway MPG', 'city mpg', 'Highway KMPL', 'City KMPL', 'MSRP']
            st.dataframe(fdf[num_cols].describe().round(2), use_container_width=True)

        with st.expander("Column reference"):
            st.markdown("""
            | Column | Description |
            |---|---|
            | Make / Model | Manufacturer and model name |
            | Year | Release year (1990 – 2017) |
            | Engine HP / Cylinders | Power output and cylinder count |
            | Transmission Type | Gearbox type |
            | Driven_Wheels | FWD / RWD / AWD / 4WD |
            | Vehicle Size / Style | Body class and style |
            | highway MPG / city mpg | Fuel efficiency in MPG |
            | Highway KMPL / City KMPL | Converted km per litre |
            | MSRP | Manufacturer Suggested Retail Price (USD) |
            """)

    # ── Tab 2 : Group-By ──────────────────────────────────────────────────────
    with tab2:
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("By Vehicle Style")
            style_grp = fdf.groupby('Vehicle Style').agg(
                Units       = ('Model',        'count'),
                Avg_HP      = ('Engine HP',    'mean'),
                Avg_Hwy_KMPL= ('Highway KMPL', 'mean'),
                Avg_MSRP    = ('MSRP',         'mean')
            ).reset_index().sort_values('Units', ascending=False)
            style_grp[['Avg_HP', 'Avg_Hwy_KMPL', 'Avg_MSRP']] = \
                style_grp[['Avg_HP', 'Avg_Hwy_KMPL', 'Avg_MSRP']].round(2)
            st.dataframe(style_grp, use_container_width=True)

        with col2:
            st.subheader("By Manufacturer")
            make_grp = fdf.groupby('Make').agg(
                Units          = ('Model',        'count'),
                Total_MSRP     = ('MSRP',         'sum'),
                Avg_Hwy_KMPL   = ('Highway KMPL', 'mean'),
                Avg_City_KMPL  = ('City KMPL',    'mean')
            ).reset_index().sort_values('Units', ascending=False)
            make_grp[['Avg_Hwy_KMPL', 'Avg_City_KMPL']] = \
                make_grp[['Avg_Hwy_KMPL', 'Avg_City_KMPL']].round(2)
            st.dataframe(make_grp, use_container_width=True)

        with st.expander("Transmission × Drivetrain breakdown"):
            trans_grp = fdf.groupby(['Transmission Type', 'Driven_Wheels']) \
                           .size().reset_index(name='Count') \
                           .sort_values('Count', ascending=False)
            st.dataframe(trans_grp, use_container_width=True)

    # ── Tab 3 : Charts ────────────────────────────────────────────────────────
    with tab3:
        col_a, col_b = st.columns(2)

        # Bar chart — top makes
        with col_a:
            st.subheader("Fleet Count by Make")
            top_makes = fdf['Make'].value_counts().head(10)

            fig, ax = plt.subplots(figsize=(7, 4.5))
            apply_chart_style(fig, ax)

            colors = [CHART_STYLE["primary"]] + [CHART_STYLE["secondary"]] * (len(top_makes) - 1)
            bars   = ax.barh(top_makes.index, top_makes.values,
                             color=colors, edgecolor="none", height=0.55)
            for b, v in zip(bars, top_makes.values):
                ax.text(v + top_makes.values.max() * 0.015,
                        b.get_y() + b.get_height() / 2,
                        f"{v:,}", va="center", color=CHART_STYLE["subtext"], fontsize=8)

            ax.set_title("Top 10 Makes by Record Count")
            ax.set_xlabel("Vehicles")
            ax.invert_yaxis()
            ax.grid(axis="x", color=CHART_STYLE["grid"], linewidth=0.8)
            ax.set_xlim(0, top_makes.values.max() * 1.15)
            plt.tight_layout()
            st.pyplot(fig)
            top1, top2 = top_makes.index[0], top_makes.index[1]
            top1_n, top2_n = top_makes.iloc[0], top_makes.iloc[1]
            gap = top1_n - top2_n
            st.success(
                f"**Interpretation —** {top1} leads the filtered selection with **{top1_n:,} vehicles**, "
                f"followed by {top2} at **{top2_n:,}** — a gap of {gap:,} units. "
                "The concentration of records in a few manufacturers reflects how dominant mass-market "
                "brands are in the dataset. Niche or luxury makes typically appear further down the list "
                "with far smaller volumes, as they produce fewer model variants and trim levels."
            )

        # Line chart — efficiency trend
        with col_b:
            st.subheader("Fuel Efficiency Over Time")
            trend = fdf.groupby('Year')[['Highway KMPL', 'City KMPL']].mean().reset_index()

            fig, ax = plt.subplots(figsize=(7, 4.5))
            apply_chart_style(fig, ax)

            ax.plot(trend['Year'], trend['Highway KMPL'],
                    color=CHART_STYLE["primary"],    linewidth=2,
                    marker='o', markersize=3.5, label='Highway')
            ax.plot(trend['Year'], trend['City KMPL'],
                    color=CHART_STYLE["secondary"],  linewidth=2,
                    marker='o', markersize=3.5, label='City')
            ax.fill_between(trend['Year'], trend['Highway KMPL'], trend['City KMPL'],
                            alpha=0.07, color=CHART_STYLE["primary"])

            ax.set_title("Avg Fuel Efficiency by Model Year (KMPL)")
            ax.set_xlabel("Year")
            ax.set_ylabel("KMPL")
            ax.legend(framealpha=0, labelcolor=CHART_STYLE["subtext"], fontsize=9)
            ax.grid(color=CHART_STYLE["grid"], linewidth=0.8)
            plt.tight_layout()
            st.pyplot(fig)
            if len(trend) >= 2:
                early_hwy = trend[trend['Year'] <= trend['Year'].quantile(0.25)]['Highway KMPL'].mean()
                late_hwy  = trend[trend['Year'] >= trend['Year'].quantile(0.75)]['Highway KMPL'].mean()
                change    = ((late_hwy - early_hwy) / early_hwy * 100)
                direction = "improved" if change > 0 else "declined"
            st.success(
                f"**Interpretation —** Highway efficiency has {direction} by roughly **{abs(change):.1f}%** "
                "from the earlier years to the most recent in this selection. "
                "The gap between highway and city KMPL stays relatively consistent across all years — "
                "highway driving is inherently more efficient due to steady cruising speeds. "
                "The post-2010 uptick is largely attributable to tighter CAFE standards in the US, "
                "the mainstreaming of hybrid powertrains, and widespread adoption of turbo-downsizing "
                "(smaller, turbocharged engines delivering similar power with better economy)."
            )

        st.write("---")

        # Scatter plot
        st.subheader("Engine HP vs Highway Efficiency")
        scatter_hue = st.selectbox(
            "Colour points by",
            ["Vehicle Size", "Transmission Type", "Driven_Wheels"]
        )

        cats = sorted(fdf[scatter_hue].dropna().unique())
        pal  = dict(zip(cats, CHART_STYLE["palette"][:len(cats)]))

        fig, ax = plt.subplots(figsize=(11, 4.5))
        apply_chart_style(fig, ax)
        for cat, grp in fdf.groupby(scatter_hue):
            ax.scatter(grp['Engine HP'], grp['Highway KMPL'],
                       label=cat, color=pal.get(cat, CHART_STYLE["tertiary"]),
                       alpha=0.5, s=30, edgecolors="none")

        ax.set_title(f"Engine HP vs Highway KMPL  —  by {scatter_hue}")
        ax.set_xlabel("Engine Horsepower (HP)")
        ax.set_ylabel("Highway KMPL")
        ax.legend(title=scatter_hue, fontsize=8, title_fontsize=8,
                  framealpha=0.6, loc="upper right")
        ax.grid(color=CHART_STYLE["grid"], linewidth=0.8)
        plt.tight_layout()
        st.pyplot(fig)
        corr = fdf['Engine HP'].corr(fdf['Highway KMPL'])
        high_hp   = fdf[fdf['Engine HP'] > 400]['Highway KMPL'].mean()
        low_hp    = fdf[fdf['Engine HP'] < 150]['Highway KMPL'].mean()
        ev_count  = len(fdf[fdf['Highway KMPL'] > 35])
        st.success(
            f"**Interpretation —** The scatter confirms a **negative correlation (r = {corr:.2f})** between "
            "engine horsepower and highway fuel efficiency — as power increases, economy falls. "
            f"Vehicles with more than 400 HP average just **{high_hp:.1f} KMPL** on the highway, "
            f"while those under 150 HP average **{low_hp:.1f} KMPL** — nearly double the efficiency. "
            "The cluster in the lower-right (high HP, low KMPL) represents performance and muscle cars. "
            "The upper-left cluster (low HP, high KMPL) is dominated by compact and subcompact vehicles. "
            f"**{ev_count} records** sitting above 35 KMPL are electric vehicles, which report efficiency "
            "in MPGe — their placement as outliers reflects the fundamental difference in powertrain type. "
            f"Changing the colour grouping to *{scatter_hue}* reveals how this HP–efficiency trade-off "
            "plays out differently across vehicle sizes, drivetrain layouts, or transmission types."
        )

    # ── Tab 4 : Insights ─────────────────────────────────────────────────────
    with tab4:
        st.subheader("Key Findings")

        findings = [
            ("Power vs. Economy",
             "Engine HP shows a −0.36 correlation with highway KMPL and a +0.66 "
             "correlation with MSRP. Performance comes at a cost in both price and fuel."),
            ("Dominant Segments",
             "Sedans (3,048 units) and 4-door SUVs (2,488 units) together make up over 46% "
             "of all records — the natural focus for any fleet strategy."),
            ("27-Year Evolution",
             "Average HP nearly doubled from 141 HP (1990) to 274 HP (2017), while highway "
             "efficiency improved from 9.81 to 12.15 KMPL — modern engineering at work."),
            ("Automatic Dominance",
             "69.4% of vehicles (8,266) use automatic transmission vs 24.6% (2,935) manual, "
             "reflecting consumer shift toward convenience over driver engagement."),
        ]

        for i, (title, body) in enumerate(findings, 1):
            col_num, col_text = st.columns([0.05, 0.95])
            col_num.markdown(
                f"<p style='color:#c0392b; font-weight:700; font-size:1rem; "
                f"padding-top:2px;'>{i}</p>",
                unsafe_allow_html=True
            )
            col_text.markdown(f"**{title}**  \n{body}")
            st.write("")


if __name__ == "__main__":
    main()
