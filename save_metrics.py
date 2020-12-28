import json
import os
import numpy as np
import matplotlib.pyplot as plt

from utils import force_decimal_places


def create_table_plot_metrics(comparison_table, json_file_path, args,
                              decimal_places, data_for_current_row,
                              graph_filename, table, output_folder,
                              time_rounded, crf_or_preset=None):
    # Make a list containing the frame numbers from the JSON file.
    with open(json_file_path, 'r') as f:
        file_contents = json.load(f)

    frame_numbers = [frame['frameNum'] for frame in file_contents['frames']]

    # Grab the VMAF data from the JSON file.
    vmaf_scores = [frame['metrics']['vmaf'] for frame in file_contents['frames']]
    mean_vmaf = force_decimal_places(np.mean(vmaf_scores), decimal_places)
    min_vmaf = force_decimal_places(min(vmaf_scores), decimal_places)
    vmaf_std = force_decimal_places(np.std(vmaf_scores), decimal_places)

    print(f'VMAF score: {mean_vmaf}, Standard Deviation: {vmaf_std}')

    # Data for the table.
    vmaf = f'{min_vmaf} | {vmaf_std} | {mean_vmaf}'

    # Plot a line showing the variation of the VMAF score throughout the video.
    print('Plotting VMAF graph...')
    plt.plot(frame_numbers, vmaf_scores, label=f'VMAF ({mean_vmaf})')
    print('Done!')
    # Add the VMAF values to the table.
    data_for_current_row.append(vmaf)

    if args.calculate_ssim:
        ssim_scores = [ssim['metrics']['ssim'] for ssim in file_contents['frames']]
        mean_ssim = force_decimal_places(round(np.mean(ssim_scores), decimal_places), decimal_places)
        min_ssim = force_decimal_places(round(min(ssim_scores), decimal_places), decimal_places)
        ssim_std = force_decimal_places(round(np.std(ssim_scores), decimal_places), decimal_places)
        ssim = f'{min_ssim} | {ssim_std} | {mean_ssim}'
        # Plot a line showing the variation of the SSIM throughout the video.
        print('Plotting SSIM graph...')
        plt.plot(frame_numbers, ssim_scores, label=f'SSIM ({mean_ssim})')
        print('Done!')
        # Add the SSIM values to the table.
        data_for_current_row.append(ssim)

    if args.calculate_psnr:
        psnr_scores = [psnr['metrics']['psnr'] for psnr in file_contents['frames']]
        mean_psnr = force_decimal_places(round(np.mean(psnr_scores), decimal_places), decimal_places)
        min_psnr = force_decimal_places(round(min(psnr_scores), decimal_places), decimal_places)
        psnr_std = force_decimal_places(round(np.std(psnr_scores), decimal_places), decimal_places)
        psnr = f'{min_psnr} | {psnr_std} | {mean_psnr}'
        # Plot a line showing the variation of the PSNR throughout the video.
        print('Plotting PSNR graph...')
        plt.plot(frame_numbers, psnr_scores, label=f'PSNR ({mean_psnr})')
        print('Done!')
        # Add the PSNR values to the table.
        data_for_current_row.append(psnr)

    plt.suptitle(graph_filename)
    plt.xlabel('Frame Number')
    plt.ylabel('Value of Quality Metric')
    plt.legend(loc='lower right')
    plt.savefig(os.path.join(output_folder, graph_filename))
    plt.clf()

    if not args.no_transcoding_mode:
        if isinstance(args.crf_value, list) and len(args.crf_value) > 1:
            data_for_current_row.insert(0, crf_or_preset)
            data_for_current_row.insert(1, time_rounded)
        # Presets comparison mode.
        else:
            data_for_current_row.insert(0, crf_or_preset)
            data_for_current_row.insert(1, time_rounded)

    table.add_row(data_for_current_row)

    # Write the table to the Table.txt file.
    with open(comparison_table, 'w') as f:
        f.write(table.get_string(title='PSNR/SSIM/VMAF values are in the format: Min | Standard Deviation | Mean'))

    print(f'The following data has been added to the table:\n{data_for_current_row}')
