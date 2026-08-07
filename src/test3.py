import flet as ft

import flet_charts as fch


class State:
    toggled = True


state = State()


def main(page: ft.Page):
    data_1 = [
        fch.LineChartData(
            stroke_width=2,
            color=ft.Colors.LIGHT_GREEN,
            curved=False,
            rounded_stroke_cap=True,

            points=[
                fch.LineChartDataPoint(0,0),
                fch.LineChartDataPoint(1, 0),
                fch.LineChartDataPoint(2, 216545211),
                fch.LineChartDataPoint(3, 312354653),
                fch.LineChartDataPoint(4, 154515122),
                fch.LineChartDataPoint(5, 548445122),
                fch.LineChartDataPoint(6, 215421445),
                fch.LineChartDataPoint(7, 564545),
                fch.LineChartDataPoint(8, 217230275),
                fch.LineChartDataPoint(9, 9727442),
                fch.LineChartDataPoint(10, 4352432),
                fch.LineChartDataPoint(11, 21010214),
            ],
        )
    ]

    data_2 = [
        fch.LineChartData(
            stroke_width=4,
            color=ft.Colors.with_opacity(0.5, ft.Colors.LIGHT_GREEN),
            rounded_stroke_cap=True,
            points=[
                fch.LineChartDataPoint(0,0),
                fch.LineChartDataPoint(1, 0),
                fch.LineChartDataPoint(2, 216545211),
                fch.LineChartDataPoint(3, 312354653),
                fch.LineChartDataPoint(4, 154515122),
                fch.LineChartDataPoint(5, 548445122),
                fch.LineChartDataPoint(6, 215421445),
                fch.LineChartDataPoint(7, 564545),
                fch.LineChartDataPoint(8, 217230275),
                fch.LineChartDataPoint(9, 9727442),
                fch.LineChartDataPoint(10, 4352432),
                fch.LineChartDataPoint(11, 21010214),
            ],
        ),
    ]

    chart = fch.LineChart(
        data_series=data_1,
        border=ft.Border(
            bottom=ft.BorderSide(4, ft.Colors.with_opacity(0.5, ft.Colors.ON_SURFACE))
        ),
        tooltip=fch.LineChartTooltip(
            bgcolor=ft.Colors.with_opacity(0.8, ft.Colors.BLUE_GREY)
        ),
        min_y=0,
        max_y=548445122,
        min_x=0,
        max_x=12,
        expand=True,
        right_axis=fch.ChartAxis(show_labels=False),
        left_axis=fch.ChartAxis(
            label_size=40,
            labels=[
                fch.ChartAxisLabel(
                    value=100000000,
                    label=ft.Text("1m", size=14, weight=ft.FontWeight.BOLD),
                ),
                fch.ChartAxisLabel(
                    value=200000000,
                    label=ft.Text("2m", size=14, weight=ft.FontWeight.BOLD),
                ),
                fch.ChartAxisLabel(
                    value=300000000,
                    label=ft.Text("3m", size=14, weight=ft.FontWeight.BOLD),
                ),
                fch.ChartAxisLabel(
                    value=400000000,
                    label=ft.Text("4m", size=14, weight=ft.FontWeight.BOLD),
                ),
                fch.ChartAxisLabel(
                    value=500000000,
                    label=ft.Text("5m", size=14, weight=ft.FontWeight.BOLD),
                ),
                fch.ChartAxisLabel(
                    value=600000000,
                    label=ft.Text("6m", size=14, weight=ft.FontWeight.BOLD),
                ),
            ],
        ),
        bottom_axis=fch.ChartAxis(
            label_size=32,
            labels=[
                fch.ChartAxisLabel(
                    value=0,
                    label=ft.Container(
                        margin=ft.Margin(top=10),
                        content=ft.Text(
                            value="JAN",
                            size=16,
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.with_opacity(0.5, ft.Colors.ON_SURFACE),
                        ),
                    ),
                ),
                fch.ChartAxisLabel(
                    value=1,
                    label=ft.Container(
                        margin=ft.Margin(top=10),
                        content=ft.Text(
                            value="FEB",
                            size=16,
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.with_opacity(0.5, ft.Colors.ON_SURFACE),
                        ),
                    ),
                ),
                fch.ChartAxisLabel(
                    value=2,
                    label=ft.Container(
                        margin=ft.Margin(top=10),
                        content=ft.Text(
                            value="MAR",
                            size=16,
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.with_opacity(0.5, ft.Colors.ON_SURFACE),
                        ),
                    ),
                ),
                fch.ChartAxisLabel(
                    value=3,
                    label=ft.Container(
                        margin=ft.Margin(top=10),
                        content=ft.Text(
                            value="APR",
                            size=16,
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.with_opacity(0.5, ft.Colors.ON_SURFACE),
                        ),
                    ),
                ),
                fch.ChartAxisLabel(
                    value=4,
                    label=ft.Container(
                        margin=ft.Margin(top=10),
                        content=ft.Text(
                            value="MAY",
                            size=16,
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.with_opacity(0.5, ft.Colors.ON_SURFACE),
                        ),
                    ),
                ),
                fch.ChartAxisLabel(
                    value=5,
                    label=ft.Container(
                        margin=ft.Margin(top=10),
                        content=ft.Text(
                            value="JUN",
                            size=16,
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.with_opacity(0.5, ft.Colors.ON_SURFACE),
                        ),
                    ),
                ),
                fch.ChartAxisLabel(
                    value=6,
                    label=ft.Container(
                        margin=ft.Margin(top=10),
                        content=ft.Text(
                            value="JUL",
                            size=16,
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.with_opacity(0.5, ft.Colors.ON_SURFACE),
                        ),
                    ),
                ),
                fch.ChartAxisLabel(
                    value=7,
                    label=ft.Container(
                        margin=ft.Margin(top=10),
                        content=ft.Text(
                            value="AUG",
                            size=16,
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.with_opacity(0.5, ft.Colors.ON_SURFACE),
                        ),
                    ),
                ),
                fch.ChartAxisLabel(
                    value=8,
                    label=ft.Container(
                        margin=ft.Margin(top=10),
                        content=ft.Text(
                            value="SEP",
                            size=16,
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.with_opacity(0.5, ft.Colors.ON_SURFACE),
                        ),
                    ),
                ),
                fch.ChartAxisLabel(
                    value=9,
                    label=ft.Container(
                        margin=ft.Margin(top=10),
                        content=ft.Text(
                            value="OCT",
                            size=16,
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.with_opacity(0.5, ft.Colors.ON_SURFACE),
                        ),
                    ),
                ),
                fch.ChartAxisLabel(
                    value=10,
                    label=ft.Container(
                        margin=ft.Margin(top=10),
                        content=ft.Text(
                            value="NOV",
                            size=16,
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.with_opacity(0.5, ft.Colors.ON_SURFACE),
                        ),
                    ),
                ),
                fch.ChartAxisLabel(
                    value=11,
                    label=ft.Container(
                        margin=ft.Margin(top=10),
                        content=ft.Text(
                            value="DEC",
                            size=16,
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.with_opacity(0.5, ft.Colors.ON_SURFACE),
                        ),
                    ),
                )
            ],
        ),
    )

    def toggle_data(e: ft.Event[ft.IconButton]):
        if state.toggled:
            chart.data_series = data_2
            chart.data_series[0].point = True
            chart.max_y = 600000000
            chart.interactive = False
        else:
            chart.data_series = data_1
            chart.max_y = 600000000
            chart.interactive = True
        state.toggled = not state.toggled
        chart.update()

    page.add(ft.IconButton(ft.Icons.REFRESH, on_click=toggle_data), chart)


ft.run(main)