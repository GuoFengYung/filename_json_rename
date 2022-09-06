# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import argparse
import json
import os
import random
import shutil
from dataclasses import dataclass
from pathlib import Path
from shutil import copyfile
from typing import List, Optional, Tuple
from tqdm import tqdm
import csv
import lxml.builder
import lxml.etree

@dataclass
class Annotation:
    @dataclass
    class Size:
        width: int
        height: int
        depth: int

    @dataclass
    class Object:
        @dataclass
        class BBox:
            left: float
            top: float
            right: float
            bottom: float

        @dataclass
        class Mask:
            color: int

        name: str
        difficult: bool
        bbox: BBox
        mask: Optional[Mask]
        polygon: List[Tuple[float, float]]

    filename: str
    size: Size
    objects: List[Object]


def read_src_annotation(path_to_annotation_json: str) -> Annotation:
    with open(path_to_annotation_json, 'r', errors='ignore') as f:
        annotation_dict = json.load(f)

    annotation = Annotation(
        filename=annotation_dict['imagePath'],
        size=Annotation.Size(
            width=annotation_dict['imageWidth'],
            height=annotation_dict['imageHeight'],
            depth=3
        ),
        objects=[Annotation.Object(
            name=shape['label'],
            difficult=shape['flags']['difficult'] if 'difficult' in shape['flags'] else False,
            bbox=Annotation.Object.BBox(
                left=float(min(p[0] for p in shape['points'])),
                top=float(min(p[1] for p in shape['points'])),
                right=float(max(p[0] for p in shape['points'])),
                bottom=float(max(p[1] for p in shape['points']))
            ),
            mask=None if shape['shape_type'] != 'polygon' else Annotation.Object.Mask(color=i + 1),  # ignore background color
            polygon=None if shape['shape_type'] != 'polygon' else [tuple(p) for p in shape['points']]
        ) for i, shape in enumerate(annotation_dict['shapes'])]
    )
    return annotation


def write_dst_annotation(annotation: Annotation, path_to_annotation_xml: str):
    E = lxml.builder.ElementMaker()

    annotation_node = E.annotation

    filename_node = E.filename
    size_node = E.size
    width_node = E.width
    height_node = E.height
    depth_node = E.depth
    object_node = E.object
    name_node = E.name
    difficult_node = E.difficult
    bbox_node = E.bbox
    left_node = E.left
    top_node = E.top
    right_node = E.right
    bottom_node = E.bottom
    mask_node = E.mask
    color_node = E.color

    root = annotation_node(
            filename_node(annotation.filename[11:]),
        size_node(
            width_node(str(annotation.size.width)),
            height_node(str(annotation.size.height)),
            depth_node(str(annotation.size.depth))
        )
    )
    for obj in annotation.objects:
        object_node_ = object_node(
            name_node(obj.name),
            difficult_node('1' if obj.difficult else '0'),
            bbox_node(
                left_node(str(obj.bbox.left)),
                top_node(str(obj.bbox.top)),
                right_node(str(obj.bbox.right)),
                bottom_node(str(obj.bbox.bottom))
            )
        )
        if obj.mask is not None:
            object_node_.append(
                mask_node(
                    color_node(str(obj.mask.color))
                )
            )
        root.append(object_node_)

    tree = lxml.etree.ElementTree(root)
    tree.write(path_to_annotation_xml, pretty_print=True)


def rename(path_to_jpg: str):
    path_to_src_jpg = sorted([path.as_posix() for path in Path(path_to_jpg).rglob(f'*.json')])
    n = 1
    for jpg in path_to_src_jpg:
        old_path = os.path.join(jpg)
        # print(old_path)
        old_name = old_path.split('/')[-1]
        os.rename(old_path, f'./new/0728_{old_name:s}')
        print(f'0728_{old_name:s}')
        n = n + 1


def convert(path_to_src_dir: str):
    path_to_src_annotation_jpgs = sorted([path.as_posix() for path in Path(path_to_src_dir).rglob(f'*.jpg')])
    print('Found {:d} JPG files'.format(len(path_to_src_annotation_jpgs)))
    filenames = []
    for path_to_src_annotation_json in tqdm(path_to_src_annotation_jpgs):
        name = path_to_src_annotation_json.split('/')[-1]
        filenames.append(name)
    print(filenames)
    with open(os.path.join(path_to_src_dir, 'val.txt'), 'w') as f:
        f.write('\n'.join(filenames))


def remove_jpg(path_to_src_dir: str, path_to_src1_dir: str):
    result = []
    with open(os.path.join(path_to_src_dir, 'val.txt'), 'r') as f:
        for line in f:
            result.append(line.strip('\n'))
    print(len(result))
    train_list = []
    with open(os.path.join(path_to_src1_dir, 'train.txt'), 'r') as f:
        for line in f:
            train_list.append(line.strip('\n'))

    for val in result:
        if val in train_list:
            train_list.remove(val)
            continue
        else:
            pass
    with open(os.path.join(path_to_src1_dir, 'train1.txt'), 'w') as f:
        f.write('\n'.join(train_list))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    def main():
        parser = argparse.ArgumentParser()
        parser.add_argument('-s', '--src_dir', type=str, required=True, help='path to source directory')
        parser.add_argument('-o', '--drc_dir', type=str, required=True, help='path to  directory')
        args = parser.parse_args()
        path_to_src_dir = args.src_dir
        path_to_drc_dir = args.drc_dir
        # convert(path_to_src_dir)
        # remove_jpg(path_to_src_dir, path_to_drc_dir)
        # rename(path_to_jpg=path_to_src_dir)
        # json_imagename_rename(path_to_src_dir, path_to_drc_dir)
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
