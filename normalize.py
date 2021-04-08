#!/usr/bin/env python

import cv2
import os

def open_img(filename):
    return cv2.imread(filename)

def global_thresholding(img):
    ret, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY) 
    return thresh

count = [0]
def find_bounding_rect(thresh):
    img, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        # get the bounding rect
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        count[0] += 1
        save_img("rectangles/" + str(count[0]) + ".jpeg", img)
    return x, y, w, h

def crop(img, x, y, w, h):
    return img[y : y + h,\
               x : x + w]


def save_img(name, img):
    cv2.imwrite(name, img)


def normalize_single_digit(src_file, out_file):
    img = open_img(src_file)
    gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    thresh = global_thresholding(gray_img)
    x,y,w,h = find_bounding_rect(thresh)
    cropped_img = crop(thresh, x, y, w, h)
    resized_img = cv2.resize(cropped_img, (8,8), interpolation = cv2.INTER_AREA) 
    save_img(out_file, resized_img)


def normalize_directory(src_dir, out_dir):
    for dirs, subdirs, files in os.walk(src_dir):
        for fname in files:
            normalize_single_digit(src_dir + "/" + fname, out_dir + "/" + fname)

def test():
    normalize_directory("raw_train_digits", "normalized_train_digits")


if __name__ == "__main__":
    test()

