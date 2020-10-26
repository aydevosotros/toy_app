{{/*
Expand the name of the chart.
*/}}
{{- define "toy.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Create a default fully qualified app name.
We truncate at 63 chars because some Kubernetes name fields are limited to this (by the DNS naming spec).
If release name contains chart name it will be used as a full name.
*/}}
{{- define "toy.fullname" -}}
{{- if .Values.fullnameOverride }}
{{- .Values.fullnameOverride | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- $name := default .Chart.Name .Values.nameOverride }}
{{- if contains $name .Release.Name }}
{{- .Release.Name | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- printf "%s-%s" .Release.Name $name | trunc 63 | trimSuffix "-" }}
{{- end }}
{{- end }}
{{- end }}

{{/*
Create chart name and version as used by the chart label.
*/}}
{{- define "toy.chart" -}}
{{- printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Common labels
*/}}
{{- define "toy.base-labels" }}
version: {{ .Chart.AppVersion | quote }}
app: {{ include "toy.name" . }}
{{- end }}

{{- define "toy.labels" -}}
app: {{ include "toy.name" . }}
version: {{ .Chart.AppVersion | quote }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
helm.sh/chart: {{ include "toy.chart" . }}
{{- end }}

{{- define "toy.db-labels" -}}
version: {{ .Chart.AppVersion | quote }}
app: {{ include "toy.name" . }}-mysql
app.kubernetes.io/name: {{ include "toy.name" . }}-mysql
app.kubernetes.io/instance: {{ .Release.Name }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
{{- end }}

{{/*
Selector labels
*/}}
{{- define "toy.selectorLabels" -}}
app: {{ include "toy.name" . }}
version: {{ .Chart.AppVersion | quote }}
app.kubernetes.io/name: {{ include "toy.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}

{{- define "toy.db-selectorLabels" -}}
app: {{ include "toy.name" . }}-mysql
app.kubernetes.io/name: {{ include "toy.name" . }}-mysql
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}

{{/*
Create the name of the service account to use
*/}}
{{- define "toy.serviceAccountName" -}}
{{- if .Values.serviceAccount.create }}
{{- default (include "toy.fullname" .) .Values.serviceAccount.name }}
{{- else }}
{{- default "default" .Values.serviceAccount.name }}
{{- end }}
{{- end }}
