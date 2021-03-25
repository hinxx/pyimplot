# 2021-03-24

Started isolating the ImPlot parts from the pyimgui.
We still need the complete ImGui C++ source to create a functional pyimplot binding.
ImGui is pinned at v1.82, ImPlot is pinned at v0.9.

## Results 1

Creating just `implot` module at the moment.
Still using all the pyimgui *.pxd, except for core.pxd.

$ python3
Python 3.9.2 (default, Mar 12 2021, 13:13:11)
[GCC 7.5.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import implot
>>> dir(implot)
['AXIS_FLAGS_AUTO_FIT', 'AXIS_FLAGS_INVERT', 'AXIS_FLAGS_LOCK', 'AXIS_FLAGS_LOCK_MAX', 'AXIS_FLAGS_LOCK_MIN', 'AXIS_FLAGS_LOD_SCALE', 'AXIS_FLAGS_NONE', 'AXIS_FLAGS_NO_DECORATIONS', 'AXIS_FLAGS_NO_GRID_LINES', 'AXIS_FLAGS_NO_LABEL', 'AXIS_FLAGS_NO_TICK_LABELS', 'AXIS_FLAGS_NO_TICK_MARKS', 'AXIS_FLAGS_TIME', 'COLOR_COUNT', 'IMPLOT_AUTO', 'IMPLOT_AUTO_COL', 'IMPLOT_VERSION', 'ImGuiError', 'PLOT_FLAGS_ANTI_ALIASED', 'PLOT_FLAGS_CANVAS_ONLY', 'PLOT_FLAGS_CROSSHAIRS', 'PLOT_FLAGS_EQUAL', 'PLOT_FLAGS_NONE', 'PLOT_FLAGS_NO_BOX_SELECT', 'PLOT_FLAGS_NO_CHILD', 'PLOT_FLAGS_NO_HIGHLIGHT', 'PLOT_FLAGS_NO_LEGEND', 'PLOT_FLAGS_NO_MENUS', 'PLOT_FLAGS_NO_MOUSE_POS', 'PLOT_FLAGS_NO_TITLE', 'PLOT_FLAGS_QUERY', 'PLOT_FLAGS_YAXIS2', 'PLOT_FLAGS_YAXIS3', 'PlotStyle', 'VERSION', 'Vec2', 'Vec4', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__version__', 'add_colormap', 'annotate', 'annotate_clamped', 'annotate_clamped_color', 'annotate_color', 'begin_drag_drop_source', 'begin_drag_drop_source_item', 'begin_drag_drop_source_x', 'begin_drag_drop_source_y', 'begin_drag_drop_target', 'begin_drag_drop_target_legend', 'begin_drag_drop_target_x', 'begin_drag_drop_target_y', 'begin_legend_popup', 'begin_plot', 'bust_color_cache', 'colormap_button', 'colormap_icon', 'colormap_scale', 'colormap_slider', 'create_context', 'destroy_context', 'drag_line_x', 'drag_line_y', 'drag_point', 'end_drag_drop_source', 'end_drag_drop_target', 'end_legend_popup', 'end_plot', 'fit_next_plot_axes', 'get_colormap_color', 'get_colormap_count', 'get_colormap_index', 'get_colormap_name', 'get_colormap_size', 'get_current_context', 'get_last_item_color', 'get_marker_name', 'get_plot_limits', 'get_plot_mouse_pos', 'get_plot_pos', 'get_plot_query', 'get_plot_size', 'get_style', 'get_style_color_name', 'hide_next_item', 'is_legend_entry_hovered', 'is_plot_hovered', 'is_plot_queried', 'is_plot_x_axis_hovered', 'is_plot_y_axis_hovered', 'item_icon_idx', 'item_icon_rgba', 'namedtuple', 'next_colormap_color', 'pixels_to_plot', 'plot', 'plot_bars1', 'plot_bars2', 'plot_barsg', 'plot_barsh1', 'plot_barsh2', 'plot_barshg', 'plot_digital', 'plot_digitalg', 'plot_dummy', 'plot_error_bars1', 'plot_error_bars2', 'plot_error_barsh1', 'plot_error_barsh2', 'plot_heatmap', 'plot_histogram', 'plot_histogram_2d', 'plot_hlines1', 'plot_image', 'plot_line1', 'plot_line2', 'plot_lineg', 'plot_pie_chart', 'plot_scatter1', 'plot_scatter2', 'plot_scatterg', 'plot_shaded1', 'plot_shaded2', 'plot_shaded3', 'plot_shadedg', 'plot_stairs1', 'plot_stairs2', 'plot_stairsg', 'plot_stems1', 'plot_stems2', 'plot_text', 'plot_to_pixels', 'plot_vlines1', 'pop_colormap', 'pop_plot_clip_rect', 'pop_style_color', 'pop_style_var', 'push_colormap', 'push_colormap_name', 'push_plot_clip_rect', 'push_style_color', 'push_style_var', 'sample_colormap', 'set_current_context', 'set_imgui_context', 'set_legend_location', 'set_mouse_pos_location', 'set_next_error_bar_style', 'set_next_fill_style', 'set_next_line_style', 'set_next_marker_style', 'set_next_plot_limits', 'set_next_plot_limits_x', 'set_next_plot_limits_y', 'set_next_plot_ticks_x', 'set_next_plot_ticks_x_range', 'set_next_plot_ticks_y', 'set_next_plot_ticks_y_range', 'set_plot_y_axis', 'show_colormap_selector', 'show_demo_window', 'show_metrics_window', 'show_style_editor', 'show_style_selector', 'show_user_guide', 'style_colors_auto', 'style_colors_classic', 'style_colors_dark', 'style_colors_light', 'warnings']
>>>

## Results 2

Reduced presence of imgui by commenting out all the unused stuff from *.pxd files.
Removed imgui_demo.cpp from compilation; had to comment out calls to in implot_demo.cpp:
ImGui::ShowFontSelector()
ImGui::ShowStyleSelector()
ImGui::ShowStyleEditor()

Not using ansifeed.pxd anymore.
Not tested with a separate pyimgui yet.

$ python3
Python 3.9.2 (default, Mar 12 2021, 13:13:11)
[GCC 7.5.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import implot
>>> dir(implot)
['AXIS_FLAGS_AUTO_FIT', 'AXIS_FLAGS_INVERT', 'AXIS_FLAGS_LOCK', 'AXIS_FLAGS_LOCK_MAX', 'AXIS_FLAGS_LOCK_MIN', 'AXIS_FLAGS_LOD_SCALE', 'AXIS_FLAGS_NONE', 'AXIS_FLAGS_NO_DECORATIONS', 'AXIS_FLAGS_NO_GRID_LINES', 'AXIS_FLAGS_NO_LABEL', 'AXIS_FLAGS_NO_TICK_LABELS', 'AXIS_FLAGS_NO_TICK_MARKS', 'AXIS_FLAGS_TIME', 'COLOR_COUNT', 'IMPLOT_AUTO', 'IMPLOT_AUTO_COL', 'IMPLOT_VERSION', 'ImGuiError', 'PLOT_FLAGS_ANTI_ALIASED', 'PLOT_FLAGS_CANVAS_ONLY', 'PLOT_FLAGS_CROSSHAIRS', 'PLOT_FLAGS_EQUAL', 'PLOT_FLAGS_NONE', 'PLOT_FLAGS_NO_BOX_SELECT', 'PLOT_FLAGS_NO_CHILD', 'PLOT_FLAGS_NO_HIGHLIGHT', 'PLOT_FLAGS_NO_LEGEND', 'PLOT_FLAGS_NO_MENUS', 'PLOT_FLAGS_NO_MOUSE_POS', 'PLOT_FLAGS_NO_TITLE', 'PLOT_FLAGS_QUERY', 'PLOT_FLAGS_YAXIS2', 'PLOT_FLAGS_YAXIS3', 'PlotStyle', 'VERSION', 'Vec2', 'Vec4', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__version__', 'add_colormap', 'annotate', 'annotate_clamped', 'annotate_clamped_color', 'annotate_color', 'begin_drag_drop_source', 'begin_drag_drop_source_item', 'begin_drag_drop_source_x', 'begin_drag_drop_source_y', 'begin_drag_drop_target', 'begin_drag_drop_target_legend', 'begin_drag_drop_target_x', 'begin_drag_drop_target_y', 'begin_legend_popup', 'begin_plot', 'bust_color_cache', 'colormap_button', 'colormap_icon', 'colormap_scale', 'colormap_slider', 'create_context', 'destroy_context', 'drag_line_x', 'drag_line_y', 'drag_point', 'end_drag_drop_source', 'end_drag_drop_target', 'end_legend_popup', 'end_plot', 'fit_next_plot_axes', 'get_colormap_color', 'get_colormap_count', 'get_colormap_index', 'get_colormap_name', 'get_colormap_size', 'get_current_context', 'get_last_item_color', 'get_marker_name', 'get_plot_limits', 'get_plot_mouse_pos', 'get_plot_pos', 'get_plot_query', 'get_plot_size', 'get_style', 'get_style_color_name', 'hide_next_item', 'is_legend_entry_hovered', 'is_plot_hovered', 'is_plot_queried', 'is_plot_x_axis_hovered', 'is_plot_y_axis_hovered', 'item_icon_idx', 'item_icon_rgba', 'namedtuple', 'next_colormap_color', 'pixels_to_plot', 'plot', 'plot_bars1', 'plot_bars2', 'plot_barsg', 'plot_barsh1', 'plot_barsh2', 'plot_barshg', 'plot_digital', 'plot_digitalg', 'plot_dummy', 'plot_error_bars1', 'plot_error_bars2', 'plot_error_barsh1', 'plot_error_barsh2', 'plot_heatmap', 'plot_histogram', 'plot_histogram_2d', 'plot_hlines1', 'plot_image', 'plot_line1', 'plot_line2', 'plot_lineg', 'plot_pie_chart', 'plot_scatter1', 'plot_scatter2', 'plot_scatterg', 'plot_shaded1', 'plot_shaded2', 'plot_shaded3', 'plot_shadedg', 'plot_stairs1', 'plot_stairs2', 'plot_stairsg', 'plot_stems1', 'plot_stems2', 'plot_text', 'plot_to_pixels', 'plot_vlines1', 'pop_colormap', 'pop_plot_clip_rect', 'pop_style_color', 'pop_style_var', 'push_colormap', 'push_colormap_name', 'push_plot_clip_rect', 'push_style_color', 'push_style_var', 'sample_colormap', 'set_current_context', 'set_imgui_context', 'set_legend_location', 'set_mouse_pos_location', 'set_next_error_bar_style', 'set_next_fill_style', 'set_next_line_style', 'set_next_marker_style', 'set_next_plot_limits', 'set_next_plot_limits_x', 'set_next_plot_limits_y', 'set_next_plot_ticks_x', 'set_next_plot_ticks_x_range', 'set_next_plot_ticks_y', 'set_next_plot_ticks_y_range', 'set_plot_y_axis', 'show_colormap_selector', 'show_demo_window', 'show_metrics_window', 'show_style_editor', 'show_style_selector', 'show_user_guide', 'style_colors_auto', 'style_colors_classic', 'style_colors_dark', 'style_colors_light', 'warnings']

## Results 3

Testing imgui and implot in a python script.
plot.pyx implements _ImGuiContext.

$ python3
Python 3.9.2 (default, Mar 12 2021, 13:13:11)
[GCC 7.5.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import imgui
>>> import implot
>>> ctx = imgui.create_context()
>>> implot.create_context()
<implot.plot._ImPlotContext object at 0x7fe3807c4e90>
>>> implot.set_imgui_context(ctx)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Argument 'ctx' has incorrect type (expected implot.plot._ImGuiContext, got imgui.core._ImGuiContext)

## Results 4

plot.pyx does not implement _ImGuiContext. Copy pyimgui core*.so next to the plot*.so.

$ python
Python 3.9.2 (default, Mar 12 2021, 13:13:11)
[GCC 7.5.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import imgui
>>> import implot
>>> ctx = imgui.create_context()
>>> implot.create_context()
<implot.plot._ImPlotContext object at 0x7f8324e24370>
>>> implot.set_imgui_context(ctx)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Argument 'ctx' has incorrect type (expected imgui.core._ImGuiContext, got imgui.core._ImGuiContext)
>>>

