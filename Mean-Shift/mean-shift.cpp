#include "opencv2/highgui/highgui.hpp"
#include "opencv2/core/core.hpp"
#include "opencv2/imgproc/imgproc.hpp"
#include <sys/types.h>
#include <dirent.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAXLINE 255

using namespace cv;

// g++ -o mean-shift mean-shift.cpp $(pkg-config opencv4 --libs --cflags)

int main(int argc, char** argv)
{
    DIR* dir;
    struct dirent* ent;

    char input_path[256];
    char output_path[256];

    strncpy(input_path, argv[1], 256);
    strncpy(output_path, argv[2], 256);

    printf("Input File : %s\n", input_path);
        
    Mat img = imread(input_path);//Read in the image, RGB three channels    
    Mat res;//Image after segmentation  
    int spatialRad = 50;//Spatial window size  
    int colorRad = 50;//color window size  
    int maxPyrLevel = 2;//The number of pyramid levels  
    pyrMeanShiftFiltering(img, res, spatialRad, colorRad, maxPyrLevel);//Color cluster smoothing filter  	
    imwrite(output_path, res);
	
    printf("%s -> %s\n",input_path, output_path);
    
    return 0;
}

