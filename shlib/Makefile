# Compile sources into shared library. Tested on Linux.


EXE = libimplot.so
#IMGUI_DIR = ../imgui-cpp
IMGUI_DIR := $(shell python -c "import os, pkg_resources; print(os.path.dirname(pkg_resources.resource_filename('imgui', 'imgui.h')))")/imguicpp
$(warning Using IMGUI_DIR $(IMGUI_DIR))
IMPLOT_DIR = ../implot-cpp
SOURCES = $(IMPLOT_DIR)/implot.cpp \
	$(IMPLOT_DIR)/implot_demo.cpp \
	$(IMPLOT_DIR)/implot_items.cpp
OBJS = $(addsuffix .o, $(basename $(notdir $(SOURCES))))
UNAME_S := $(shell uname -s)

CXXFLAGS = -I$(IMGUI_DIR) -I$(IMPLOT_DIR)
CXXFLAGS += -g -Wall -Wformat -fPIC
# XXX: handle Windows/MacOS
LIBS = -Wl,-rpath,'$$ORIGIN'

ifeq ($(UNAME_S), Linux) #LINUX
	ECHO_MESSAGE = "Linux"
	CFLAGS = $(CXXFLAGS)
endif

ifeq ($(UNAME_S), Darwin) #APPLE
	ECHO_MESSAGE = "Mac OS X"
	CFLAGS = $(CXXFLAGS)
endif

ifeq ($(OS), Windows_NT)
	ECHO_MESSAGE = "MinGW"
	CFLAGS = $(CXXFLAGS)
endif

%.o:$(IMPLOT_DIR)/%.cpp
	$(CXX) $(CXXFLAGS) -c -o $@ $<

all: $(EXE)
	@echo Build complete for $(ECHO_MESSAGE)

$(EXE): $(OBJS)
	$(CXX) -shared -o $@ $^ $(CXXFLAGS) $(LIBS)

clean:
	rm -f $(EXE) $(OBJS)
