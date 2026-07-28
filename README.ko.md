# dsu-class

DSU 수업에서 사용하는 하드웨어 제어/센서 실습용 Python 스크립트 모음입니다.  
LED, 디스플레이, 모터, 스피커 같은 출력 장치와 IMU, ToF, 다이얼, 환경 센서 입력을 단계별로 연습할 수 있도록 구성되어 있습니다.

## 개요

이 저장소는 `python/` 폴더 아래에 **작은 단위의 독립 실행 스크립트**로 구성되어 있습니다.  
파일명은 보통 수업 순서에 맞춰 `1_*`, `2_*`, `3_*`, `4_*` 형태로 나뉘며, 각 파일이 하나의 기능/미션에 집중합니다.

## 저장소 구조

```text
python/
  1_display1.py       # 디스플레이 출력 기초
  1_led1.py           # LED 제어 기초
  1_led_mission1.py   # LED 미션/응용
  1_motor.py          # 모터 제어 기초
  1_speaker.py        # 스피커(버저) 출력
  2_IMU.py            # IMU 센서 값 읽기
  2_Tof.py            # ToF 거리 센서 읽기
  2_dials.py          # 다이얼/노브 입력 처리
  2_envs.py           # 환경 센서 값 읽기
  3_t1.py ~ 3_t4.py   # 3단계 과제/통합 실습
  4_t1.py             # 4단계 과제/통합 실습
  guehean.py          # 개별 실습 스크립트
  hanbal.py           # 개별 실습 스크립트
  hello.py            # 기본/종합 테스트 스크립트
```

## 실행 환경

- Python 3.8 이상 권장
- 수업에서 사용하는 보드/센서에 맞는 Python 라이브러리
- DSU 수업 하드웨어 환경(보드, 연결된 센서/모듈)

> 현재 저장소에는 `requirements.txt` 또는 `pyproject.toml`이 없으므로,
> 패키지 설치는 수업 환경(이미지/매뉴얼)에 맞춰 진행해야 합니다.

## 빠른 시작

저장소를 클론한 뒤, 원하는 스크립트를 직접 실행하세요.

```bash
git clone https://github.com/Mccomack/dsu-class.git
cd dsu-class/python
python hello.py
```

특정 수업 파일 실행 예시:

```bash
python 1_led1.py
python 2_IMU.py
python 3_t4.py
```

## 권장 학습 순서

1. `1_*` 파일로 출력 제어 기초(LED/디스플레이/모터/스피커)
2. `2_*` 파일로 센서 입력 기초(IMU/ToF/다이얼/환경)
3. `3_*`, `4_*` 파일로 통합 과제 수행
4. `hello.py`, `guehean.py`, `hanbal.py`로 추가 실험

## 참고

- 이 저장소는 패키지형 애플리케이션보다는 **개별 실행 실습 파일 중심**입니다.
- `python/__pycache__/`는 실행 시 생성되는 캐시 파일이므로 무시해도 됩니다.

## 개선 제안

- `requirements.txt` 추가(의존성 버전 명시)
- 각 파일 상단에 하드웨어 연결/핀맵/목적 주석 보강
- 실습 결과 스크린샷 또는 데모 영상 링크 추가
- 공개 배포 목적이라면 `LICENSE` 파일 추가
