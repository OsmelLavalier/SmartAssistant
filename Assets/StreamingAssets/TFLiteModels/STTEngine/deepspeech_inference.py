# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.

# The Original Code is Copyright (C) 2020 Voxell Technologies.
# All rights reserved.

import tensorflow as tf
# from tensorflow_asr.featurizers.speech_featurizers import read_raw_audio

tflitemodel = tf.lite.Interpreter(model_path="./deepspeech-0.9.3-models.tflite")

input_details = tflitemodel.get_input_details()
output_details = tflitemodel.get_output_details()

print("=== INPUT ===")
for detail in input_details:
  print(detail)
print("=== OUTPUT ===")
for detail in output_details:
  print(detail)