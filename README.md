# pyimplot

Python bindings for the amazing
[ImPlot](https://github.com/ocornut/imgui), GPU accelerated plotting library for
[Dear ImGui](https://github.com/ocornut/imgui).

        Warning: This is alpha quality code.

Documentation: TODO

# ImPlot

NOTES from the time when this was introduced into the pyimgui codebase!

It is not clear to me if this is the best place for ImPlot python binding. The
question remains if it would be better to place this code into a separate project,
or provide it as part of pyimgui. As of now the latter has been chosen due to my
laziness, poor undestanding of cython and also due to some obstacles
encountered during the process of creating this binding.

Read on if you are interested in couple of details.

As per ImGui and ImPlot documentation using them both as shared library is not recomended.
In case of python binding this is exactly what is being done. The ImGui part ends up being
a shared library and plot becomes a separate shared library. Creating a single shared library
(with ImGui and ImPlot) does not sound like a good idea at all so lets not go there. Not going
with shared library is also something that we can not do; AFAICT due to the way cypthon does
its business (I might be wrong).

At the level of C++ that cython wraps into python module and functions, ImPlot want access
to `imgui.h` and `imgui_internal.h`. For example ImPlot uses `ImTextureID`, `ImGuiCond`,
`ImGuiMouseButton`, `ImGuiKeyModFlags`, `ImGuiDragDropFlags`, `ImU32`, `ImDrawList`, `ImGuiContext`,
`ImVec2`, `ImVec4` and alike. These need to be exposed a cython level, too. Currently,
these come from `cimgui` and `internal` modules provided by pyimgui binding. Using them is
as simple as adding a `cimport` line to a `cimplot.pxd`. pyimgui (c)imports were requiered for
`plot.pyx` as well:

        cimport cimplot
        cimport cimgui
        cimport core
        cimport enums

If the ImPlot is placed in a separate project/repo these would need to be redefined.


When I tried to compile the ImPlot C++ code for cython binding (without adding ImGui sources)
for that shared library, doing `import imgui` in a user script fails with `GImGui` being undefined.
Have I missed something there during the library build?! I don't know.

If the ImPlot binding is separate from ImGui binding (cleanest approach), I'm not sure how
the user script would behave if pyimgui and pyimplot would be based of different ImGui C++ code.
Might be a non-issue, but I just do not know.

Have any ideas or suggestions on the above topics? Bring them up, please!


# Development tips

In order to build and install project locally ,ake sure you have created and
activated virtual environment using `virtualenv` or `python -m venv` (for newer
Python releases). Then you can just run:

    make build

This command will bootstrap whole environment (pull git submodules, install
dev requirements etc.) and build the project. `make` will automatically install
`implot` in the *development/editable* mode.
