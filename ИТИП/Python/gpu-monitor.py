#!/usr/bin/env python3

import json
import subprocess
import re
import psutil

def get_cpu_usage():
    """Получить загрузку CPU в процентах"""
    return psutil.cpu_percent(interval=1)

def get_cpu_temp():
    """Получить температуру CPU"""
    try:
        temps = psutil.sensors_temperatures()
        if 'coretemp' in temps:
            return max([temp.current for temp in temps['coretemp']])
        elif 'k10temp' in temps:
            return max([temp.current for temp in temps['k10temp']])
    except:
        pass
    
    try:
        with open('/sys/class/thermal/thermal_zone0/temp', 'r') as f:
            temp = int(f.read().strip()) / 1000.0
            return temp
    except:
        return None

def get_gpu_info():
    """Получить информацию о GPU через rocm-smi"""
    try:
        result = subprocess.run(['/opt/rocm/bin/rocm-smi', '--showtemp', '--showuse'], 
                              capture_output=True, text=True, timeout=5)
        output = result.stdout
        
        # Парсим температуру (junction temperature)
        temp_match = re.search(r'Temperature \(Sensor junction\) \(C\):\s*([\d.]+)', output)
        gpu_temp = float(temp_match.group(1)) if temp_match else None
        
        # Парсим использование GPU
        usage_match = re.search(r'GPU use \(%\):\s*(\d+)', output)
        gpu_usage = int(usage_match.group(1)) if usage_match else None
        
        return gpu_usage, gpu_temp
    except Exception as e:
        return None, None

def main():
    cpu_usage = get_cpu_usage()
    cpu_temp = get_cpu_temp()
    gpu_usage, gpu_temp = get_gpu_info()
    
    # Форматируем вывод
    cpu_text = f"CPU: {cpu_usage:.1f}%"
    if cpu_temp:
        cpu_text += f" {cpu_temp:.0f}°C"
    
    gpu_text = ""
    if gpu_usage is not None:
        gpu_text = f" GPU: {gpu_usage}%"
    if gpu_temp is not None:
        if not gpu_text:  # Если использование не найдено, но температура есть
            gpu_text = " GPU:"
        gpu_text += f" {gpu_temp:.0f}°C"
    
    output_text = f"{cpu_text}{gpu_text}"
    
    output = {
        "text": output_text
    }
    
    print(json.dumps(output))

if __name__ == "__main__":
    main()