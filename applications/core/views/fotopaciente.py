from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Q
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from applications.core.models import FotoPaciente
from applications.core.forms.fotopaciente import FotoPacienteForm
from applications.security.components.mixin_crud import PermissionMixin, ListViewMixin, CreateViewMixin, UpdateViewMixin, DeleteViewMixin

class FotoPacienteListView(PermissionMixin, ListViewMixin, ListView):
    model = FotoPaciente
    template_name = 'core/fotopaciente/list.html'
    context_object_name = 'fotospaciente'
    permission_required = 'view_fotopaciente'

    def get_queryset(self):
        q1 = self.request.GET.get('q')
        if q1:
            self.query.add(Q(paciente__nombres__icontains=q1) | Q(paciente__apellidos__icontains=q1), Q.OR)
        return self.model.objects.filter(self.query).order_by('-fecha')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('core:fotopaciente_create')
        return context

class FotoPacienteCreateView(PermissionMixin, CreateViewMixin, CreateView):
    model = FotoPaciente
    form_class = FotoPacienteForm
    template_name = 'core/fotopaciente/form.html'
    success_url = reverse_lazy('core:fotopaciente_list')
    permission_required = 'add_fotopaciente'

    def form_valid(self, form):
        messages.success(self.request, 'Foto del paciente registrada correctamente.')
        return super().form_valid(form)

class FotoPacienteUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
    model = FotoPaciente
    form_class = FotoPacienteForm
    template_name = 'core/fotopaciente/form.html'
    success_url = reverse_lazy('core:fotopaciente_list')
    permission_required = 'change_fotopaciente'

    def form_valid(self, form):
        messages.success(self.request, 'Foto del paciente actualizada correctamente.')
        return super().form_valid(form)

class FotoPacienteDeleteView(PermissionMixin, DeleteViewMixin, DeleteView):
    model = FotoPaciente
    template_name = 'core/delete.html'
    success_url = reverse_lazy('core:fotopaciente_list')
    permission_required = 'delete_fotopaciente'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Eliminar Foto'
        context['description'] = f"¿Desea eliminar la foto del paciente: {self.object.paciente} del {self.object.fecha.strftime('%Y-%m-%d')}?"
        context['back_url'] = self.success_url
        return context
